test = {
  'name': 'Question 2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # your answer should be a table 
          >>> from datascience import *
          >>> type(stats_table) == Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Be sure the names of your columns are exactly as expected.
          >>> stats_table.labels == ("Class", "Survival Rate", "Mean Age", "Percentage")
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