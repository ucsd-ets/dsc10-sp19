test = {
  'name': 'Question 5_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check your column names, number of rows, and make sure row and column numbers are in the correct range. 
          >>> daily_double_coordinates.labels[0] == 'row' and daily_double_coordinates.labels[1] == 'column'
          True
          >>> daily_double_coordinates.column(0).item(0) in np.arange(5)+1 and daily_double_coordinates.column(1).item(0) in np.arange(6)+1
          True
          >>> daily_double_coordinates.num_rows == 10
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