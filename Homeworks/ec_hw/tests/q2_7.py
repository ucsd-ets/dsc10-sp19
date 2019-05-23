test = {
  'name': 'Question 2_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your function should pass this test.
          >>> from datascience import *
          >>> test = Table().with_column('Recommended',['Yes','Yes'])
          >>> majority(test) == 'Yes'
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
