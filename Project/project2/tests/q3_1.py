test = {
  'name': 'Question 3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your array should sum to 1 with 5 element.
          >>> abs(triple_stumpers_by_row_j.sum() - 1) <= 0.001
          True
          >>> abs(triple_stumpers_by_row_dj.sum() - 1) <= 0.001
          True
          >>> triple_stumpers_by_row_j.size == 5
          True
          >>> triple_stumpers_by_row_dj.size == 5
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