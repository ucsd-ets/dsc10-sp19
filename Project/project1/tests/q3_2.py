test = {
  'name': 'Question 3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Each rate should be between 0 and 100.
          >>> 0 <= first_class_women_survival_rate <= 100
          True
          >>> 0 <= second_class_women_survival_rate <= 100
          True
          >>> 0 <= third_class_women_survival_rate <= 100
          True
          >>> 0 <= first_class_men_survival_rate <= 100
          True
          >>> 0 <= second_class_men_survival_rate <= 100
          True
          >>> 0 <= third_class_men_survival_rate <= 100
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
