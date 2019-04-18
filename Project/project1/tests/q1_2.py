test = {
  'name': 'Question 1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # your answer should be a table
          >>> from datascience import *
          >>> type(titanic) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Be sure the name of your columns are exactly as expected.
          >>> titanic.labels == ('Survived','Pclass','Name','Sex','Age','Siblings/Spouses Aboard','Parents/Children Aboard','Fare','First Name','Title')
          True
          >>> # Make sure to define your function extract_title correctly
          >>> # It should take a string as an input and return the first word in the string
          >>> isinstance(extract_title('haha haha'),str)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
