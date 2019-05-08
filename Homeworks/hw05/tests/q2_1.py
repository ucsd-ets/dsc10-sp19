test = {
  'name': 'Question 2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(choosing_pets, Table)
          True
          >>> callable(choose_pet)
          True
          >>> isinstance(choose_pet(choosing_pets,8,3,7,10), list)
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
