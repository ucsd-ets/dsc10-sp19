test = {
  'name': 'Question 1_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # your answer should be a number
          >>> 0 <= revenue_dollars <= 4000000
          True
          >>> # your answer should have two decimal place
          >>> len(str(revenue_dollars)) - str(revenue_dollars).index('.') - 1
          2
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
