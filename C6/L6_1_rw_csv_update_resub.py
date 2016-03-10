__author__ = 'Hernan Y.Ke'
import csv, os
from collections import namedtuple
import shutil

# naive
with open(os.getcwd() + '\\k.csv') as f:
    fcsv = csv.reader(f, delimiter=',')
    heading = next(fcsv)
    for r in fcsv:
        print(r)
    f.close()



#using namedtuple
with open(os.getcwd() + '\\k.csv') as f:
    fcsv = csv.reader(f)
    heading = next(fcsv)
    Row = namedtuple('Row', heading)
    for r in fcsv:
        row = Row(*r)
        print(row)
    f.close()

#better
with open(os.getcwd() + '\\k.csv') as f:
    fcsv = csv.DictReader(f)
    for r in fcsv:
        print(r['age'])
    f.close()

print('---')

# below are write methods. write using tuples or dicts

headertuple = ['name', 'age', 'gen']
rowtuple = [("a", 12, 'm'), ('b', 24, 'f'), ]
rowdict = [{'name': 'a', 'age': 12, 'gen': 'm'}, {'name': 'b', 'age': 24, 'gen': 'f'}]

with open(os.getcwd() + '\\s.csv', 'w') as f:  # to eliminate new line, also can add kwargs newlinw='\n'

    fcsv = csv.writer(f, quotechar='\'', quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')  # works.
    fcsv.writerow(headertuple)
    fcsv.writerows(rowtuple)
    f.close()

    # with open(os.getcwd()+'\\s.csv','w+') as f:
    #
    #     fcsv = csv.DictWriter(f,headertuple)
    #     fcsv.writeheader()
    #     fcsv.writerows(rowdict)
    #     f.close()


# To be continued