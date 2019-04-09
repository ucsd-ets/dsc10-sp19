test = {
  'name': 'Question 6_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(total_fruit_sold, int) or isinstance(total_fruit_sold, np.int64)
          True
          """,
          'hidden': False,
          'locked': False
        }, 
        {
          'code': r"""
          >>> # We're asking for the number of *pieces* of fruit, not the
          >>> # number of kinds of fruit or the number of boxes from which
          >>> # there were sales.
          >>> total_fruit_sold > 10
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
