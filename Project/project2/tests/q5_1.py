test = {
  'name': 'Question 5_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer should be a list with numbers 1 through 8.
          >>> isinstance(q_5_1_answer, list)
          True
          >>> q_5_1_answer[0] in np.arange(8)+1
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