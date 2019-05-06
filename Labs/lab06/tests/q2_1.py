test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> old = full_data.with_column('Age', full_data.column('Age')*3)
          >>> np.max(histograms(old)[0]) == np.max(old.column('Age')) + 1
          True
          >>> np.min(histograms(old)[0]) == np.min(old.column('Age'))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.max(histograms(full_data)[1]) > np.max(full_data.column('Salary'))
          True
          >>> np.min(histograms(full_data)[1]) == np.min(full_data.column('Salary'))
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
