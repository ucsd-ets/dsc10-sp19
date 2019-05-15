test = {
  'name': 'Question 3_14',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer should sum to 1 with 6 element.
          >>> abs(asked_column_dist.sum() - 1)<0.001
          True
          >>> asked_column_dist.size==6
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