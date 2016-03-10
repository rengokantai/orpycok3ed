__author__ = 'Hernan Y.Ke'
import sqlite3

names=[('ke',),('he',)]     #must be tuple.
db = sqlite3.connect('db.ke')
c =db.cursor()
c.execute('create table ketable(name text)')
db.commit()
c.executemany('insert into ketable values (?)',names)   #syntax!
db.commit()

for row in db.execute('select * from ketable'):
    print(row)
print('------')
h = 'he'
for row in db.execute('select * from ketable where name = ?',(h,)):  #must has trailing comma ,syntax
    print(row)
