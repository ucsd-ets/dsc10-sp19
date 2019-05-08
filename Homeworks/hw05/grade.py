"""
This program gets the submissions for the assignment set in the .ok file
and grades it using the tests specified in that file as well. The scores
are output to a .csv file where each row contains the backup ID, numeric
score, and the output of the tests.

Before running, you will need to install the following dependencies:
 * requests
 * nbformat
 * nbconvert

You can run the following command to install them:
pip install requests nbformat nbconvert
"""
import json
import re
import glob
import csv
import argparse
import concurrent.futures
import nbformat
import requests
from nbconvert.preprocessors import ExecutePreprocessor

# The maximum time in seconds to grade a notebook.
TEST_TIMEOUT = 600

# A list of strings containing additional tests to run at the end of the
# notebook. This is useful if the assignment is missing some tests.
# 
# For example: EXTRA_TESTS = ['q24', 'q25'] means tests/q24.py and tests/q25.py
# will be ran and scored.
EXTRA_TESTS = ['q2', 'q5_2', 'q5_4', 'q1_12', 'q1_13', 'q4_22', 'q4_32', 'q5_42', 'q5_43']

# A list of strings containing the tests to skip. This is useful if there are
# some tests that take too long to run or are not neccessary.
#
# For example: SKIP_TESTS = ['q1', 'q2'] means tests/q1.py and tests/q2.py will
# be skipped.
SKIP_TESTS = ['q5_1', 'q5_3']

# Each correct test case gives SCORE_MULTIPLIER points.
SCORE_MULTIPLIER = 1

# The variable used to grade the notebook. This corresponds to whatever goes
# before the "= Notebook('<assignment>.ok')". For example, if you have
# proj2 = Notebook('project2.ok'), you should set NOTEBOOK_VAR = 'proj2'. 
NOTEBOOK_VAR = 'ok'

# 
CUSTOM_ANSWERS = {
}

# Regex pattern for finding the total score.
TOTAL_PATTERN = r"{['\"]Total['\"]: ([-+]?[0-9]*\.?[0-9]*)}"
GRADE_PATTERN_PRE = re.compile(r"_ = ([\w_]+)\.grade\([\\]*['\"](\w+)[\\]*['\"]\)")
GRADE_PATTERN2 = re.compile(r"([\w_]+)\.grade\([\\]*['\"](\w+)[\\]*['\"]\)(;*)")
GRADE_PATTERN = re.compile(r"\.grade\([\\]*['\"](\w+)[\\]*['\"]\)")
GRADE_REPLACE_PATTERN = r"\1.grade('\2')"
GRADE_REPLACE_PATTERN2 = r"_test = \1.grade('\2'); _test"

def get_cells_between(cells, start, end):
    """
    Returns a list of cells between the cell that contains the string start and
    the cell that contains the string end. The cells parameter refers to the
    cells of a notebook. Given a notebook nb, you can access its cells with
    `nb.cells`.

    For example, if you want to get the cells between a cell that contains the
    word "Question 1" and a cell that contains "Question 3" (i.e. you want to
    get the cells between Question 1 and Question 3), you would use:
    get_cells_between(cells, 'Question 1', 'Question 3')
    """
    start_index = None
    end_index = None

    for index, cell in enumerate(cells):
        if start_index is None and start in cell['source']:
            start_index = index
        elif start_index is not None and end in cell['source']:
            end_index = index

            break

    if start_index and end_index:
        return cells[start_index:end_index]
    
    return []

def skip_cells_between(cells, start, end):
    """
    Given a list of cells, this function returns `cells` with the cells between
    a cell that contains the string `start` and a cell that contains the string
    `end` removed.

    For example, suppose you have cell A that contains the string "Question 4"
    and another cell B that contains the string "Question 6". If you want remove
    any cells between A and B (inclusive), then you would use:
    skip_cells_between(cells, 'Question 4', 'Question 6')
    """
    start_index = None
    end_index = None

    for index, cell in enumerate(cells):
        if start_index is None and start in cell['source']:
            start_index = index
        elif start_index is not None and end in cell['source']:
            end_index = index

            break

    if start_index and end_index:
        return cells[:start_index] + cells[end_index:]
    
    return cells

def preprocess_notebook(notebook):
    """
    Turns the notebook JSON into an executable notebook for grading.
    """
    # Get rid of submission/authentication/grade cells.
    notebook = notebook.replace('_ = ' + NOTEBOOK_VAR + '.submit()', '') \
                       .replace('_ = ' + NOTEBOOK_VAR + '.auth(inline=True)', '') \
                       .replace(NOTEBOOK_VAR + '.score()', '')
    notebook = re.sub(GRADE_PATTERN_PRE, GRADE_REPLACE_PATTERN, notebook)
    notebook = re.sub(GRADE_PATTERN2, GRADE_REPLACE_PATTERN2, notebook)

    # Load the notebook file.
    nb = nbformat.reads(notebook, as_version=4)

    # Create cells the store custom answers.
    last_cell = None
    index = 0

    for save_to, keywords in CUSTOM_ANSWERS.items():
        # Handle custom answers that are cells between two keywords.
        # That is, elements that are tuples (save_to_variable, start, end).
        if isinstance(keywords, tuple):
            source = save_to + ' = ' + str(get_cells_between(nb.cells, keywords[0], keywords[1]))
            answer_cell = nbformat.v4.new_code_cell(source)
            nb.cells.append(answer_cell)

    while index < len(nb.cells):
        cell = nb.cells[index]

        for keyword, save_to in CUSTOM_ANSWERS.items():
            if isinstance(save_to, tuple):
                continue

            if last_cell is not None and keyword in cell['source']:
                # Handle custom answers that use a callback to store an answer.
                if 'function' in str(type(save_to)):
                    results = save_to(last_cell)

                    if results is not None:
                        answer_cell = nbformat.v4.new_code_cell(results)
                        nb.cells.insert(index, answer_cell)
                        index += 1
                # Handle custom answers that just store a plain value.
                else:
                    source = save_to + ' = ' + str(last_cell)
                    answer_cell = nbformat.v4.new_code_cell(source)
                    nb.cells.insert(index, answer_cell)
                    index += 1

                break

        index += 1
        last_cell = cell

    # Add a cell to run the tests and get a score.
    for extra_test in EXTRA_TESTS:
        extra_cell = nbformat.v4.new_code_cell(NOTEBOOK_VAR + ".grade('" + extra_test + "')")
        nb.cells.append(extra_cell)

    return nb

def test_notebook(notebook):
    """
    Executes the given notebook and outputs the test results using
    OK's scoring function. The score is returned as a float and
    the output of the test as a string.
    """
    output_total = 0

    nb = preprocess_notebook(notebook)

    # Run the notebook.
    execute = ExecutePreprocessor(timeout=TEST_TIMEOUT, kernel_name='python3')
    execute.allow_errors = True
    execute.preprocess(nb, {'metadata': {'path': './'}})

    # Get the score and test results at the bottom.
    scores = {}

    output_text = []

    for cell in nb.cells:
        # Look at cells that run a test case.
        if cell['cell_type'] != 'code':
            continue

        match = GRADE_PATTERN.search(cell['source'])

        if match is None:
            continue

        test_case = match.group(1)

        if test_case in scores or test_case in SKIP_TESTS:
            continue

        scores[test_case] = 0
        output_text.append('Grading ' + test_case + ':')

        for output in cell['outputs']:
            if output['output_type'] == 'stream':
                # Clean up any Ok output.
                text = output['text']
                text = text.replace('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n', '') \
                           .replace('Running tests\n', '')

                output_text.append(text)
            elif output['output_type'] == 'execute_result':
                # Record scores for any tests that were ran.
                text = output['data']['text/plain']

                if "'failed': 0" in text:
                    scores[test_case] = SCORE_MULTIPLIER
                    output_total += SCORE_MULTIPLIER
            elif output['output_type'] == 'error':
                # Record any errors that occured while grading.
                text = '\n' + output['ename'] + ': ' + output['evalue'] + '\n'
                text += '\n'.join(output['traceback'])
                text += '\n'

                output_text.append(text)
                        
    if not output_text or output_total is None:
        return -1, ''

    # Add a score breakdown at the end of the grade message.    
    output_text.append('\nScore Breakdown:')        

    for test_case in sorted(scores.keys()):
        output_text.append('\n\t' + test_case + ': ' + str(scores[test_case]) + '/' + str(SCORE_MULTIPLIER))

    output_text.append('\n\nTotal: ' + str(output_total))

    # Output the total score and the output from the tests.
    return output_total, ''.join(output_text)

def grade_backup(backup):
    """
    Given a backup, the notebook file for the assignment is found
    and graded. The backup's ID, numeric score, and output
    from grading is returned.
    """
    # Find the Python notebook.
    notebook = ''

    if not backup['messages']:
        return

    print('Grading ' + backup['id'] + '...')

    for path, contents in backup['messages'][0]['contents'].items():
        if 'ipynb' in path:
            notebook = contents

            break

    if not notebook:
        print('Failed to find notebook for backup ' + backup['id'])

        return

    # Score the notebook.
    score = -1

    try:
        score, output = test_notebook(notebook)
    except:
        score = -1

    if score == -1:
        print('Failed to score ' + backup['id'])

        return

    return backup['id'], score, output

def get_scores(token, end_point, limit=150):
    """
    Finds all submissions for the given assignment (the end point) and
    grades them. The scores are returned as a list of lists containing
        1. The backup ID
        2. The numeric score
        3. The output of the tests
    """
    # Request all of the final submissions.
    url = 'https://okpy.org/api/v3/assignment/{}/submissions?access_token={}&limit={}'
    url = url.format(end_point, token, limit)

    res = requests.get(url)
    data = json.loads(res.text)

    assert data['code'] == 200

    # Score each backup [backup id, score, test output] and return all the scores.
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(grade_backup, data['data']['backups'])
        
        return [result for result in results if result is not None and result[0] is not None]

def get_endpoint():
    """
    Scans the current directory for an .ok file and gets the endpoint from it.
    """
    # We want the endpoint key in the .ok file.
    files = glob.glob('*.ok')

    if not files:
        return

    with open(files[0]) as ok_file:
        ok_data = json.loads(ok_file.read())

        return ok_data['endpoint']

def grade(token, limit, endpoint, output_path):
    """
    Grades all of the submissions for the given assignment and writes
    the scores to the given output path.
    """
    # Get values for the token, output, and endpoint.
    if not token:
        token = input('Enter your OK token: ')

    if not output_path:
        output_path = 'scores.csv'

    endpoint = get_endpoint()

    if not endpoint:
        endpoint = input('Enter the desired endpoint: ')

    # Grade the assignment and write the results to the desired
    # output .csv file.
    print('Scoring ' + endpoint)

    if limit:
        print('Limit set to ' + str(limit))

    with open(output_path, 'w', newline='') as scores_file:
        writer = csv.writer(scores_file)
        writer.writerows(get_scores(token, endpoint, limit))

        print('Scores have been written to ' + output_path)

def grade_input(input_path):
    print('Grading ' + input_path)

    with open(input_path, 'r') as input_file:
        score, output = test_notebook(input_file.read())

        if score == -1:
            print('Failed to grade ' + input_path)
        else:
            print(output)
            print('SCORE: ' + str(score))

def main():
    """
    The driver for the grading script.
    """
    parser = argparse.ArgumentParser(description='OK grading script')
    parser.add_argument('--token', help='access token for OK')
    parser.add_argument('--output', help='where to output scores to')
    parser.add_argument('--endpoint', help='the endpoint for the assignment to grade')
    parser.add_argument('--limit', help='how many submissions to grade', type=int)
    parser.add_argument('--input', help='input notebook to test')

    args = parser.parse_args()

    if args.input is not None:
        grade_input(args.input)
    else:
        grade(token=args.token, \
            limit=args.limit, \
            endpoint=args.endpoint, \
            output_path=args.output)

if __name__ == '__main__':
    main()
