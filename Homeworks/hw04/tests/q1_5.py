test = {
  'name': 'Question 1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> callable(lastname_length)
          True
          >>> lastname_length('Tiefenbruck, Janine') == "normal"
          True
          >>> lastname_length('Schwinghammer, Rob') == "very long"
          True
          >>> lastname_length('Fan, Shicheng') == "very short"
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
