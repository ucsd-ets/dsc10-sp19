test = {
  'name': 'Question 5_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # least_popular_names should be an array, and least_popular_name_count should be a number
          >>> import numpy as np
          >>> type(least_popular_names) == np.ndarray
          True
          >>> 0 <= least_popular_name_count <= 100
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