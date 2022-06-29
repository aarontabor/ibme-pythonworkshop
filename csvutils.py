'''
`csvreader` and `csvwriter` provide low-level functionality for csv files.
However, sometimes we want to work more abstractly.
`DictReader` / `DictWriter` take care of many data transformations for us.
'''

from csv import DictReader, DictWriter

# Using a DictReader imports data as a list of dictionaries.
# Dictionary keys correspond to column headers
contacts = DictReader(open('data/contacts.csv', 'r'))

# for contact in contacts:
#   print(f'{column.first} {column.last}')


# DictWriter allows us to export data using the same formatting (a list of dictionaires)
from classes import Point

points = [Point.generate_random_point() for i in range(10)]

# __dict__ is a "dunder field" - it is where all of the objects fields are stored 
point_dicts = [p.__dict__ for p in points]

writer = DictWriter(open('data/points.csv', 'w'), fieldnames=['x', 'y'])
writer.writeheader()
writer.writerows(point_dicts)

# ...alternately:
#   for p in points:
#     writer.writerow(p.__dict__)