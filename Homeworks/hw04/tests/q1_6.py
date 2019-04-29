test = {
  'name': 'Question 1_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(last_names, Table)
          True
          >>> set(last_names.labels) == {"Athlete", "Country", "Gender", "Medal", "Long Last Name?"}
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
