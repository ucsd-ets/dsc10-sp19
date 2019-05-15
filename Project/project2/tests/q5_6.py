test = {
  'name': 'Question 5_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your table should be formatted like the table in the previous question. 
          >>> watson_coordinates.labels[0] == 'row' and watson_coordinates.labels[1] == 'column'
          True
          >>> watson_coordinates.column(0).item(0) in np.arange(5)+1 and watson_coordinates.column(1).item(0) in np.arange(6)+1
          True
          >>> watson_coordinates.num_rows == 10
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