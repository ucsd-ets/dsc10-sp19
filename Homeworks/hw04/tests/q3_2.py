test = {
  'name': 'Question 3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(grades, np.ndarray)
          True
          >>> "A+" in grades
          True
          >>> "A" in grades
          True
          >>> "B" in grades
          True
          >>> "C" in grades
          True
          >>> "D" in grades
          True
          >>> "F" in grades
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
