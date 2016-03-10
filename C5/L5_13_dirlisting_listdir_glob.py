__author__ = 'Hernan Y.Ke'
import os,glob

names = [i for i in os.listdir(os.path.abspath(os.getcwd())) if os.path.isfile(os.path.join(os.path.abspath(os.getcwd()),i))]
print(names)

#same as
pyname = [i for i in os.listdir(os.path.abspath(os.getcwd())) if os.path.isfile(i)]
print(pyname)


#using glob and stat
pyfile=glob.glob('*.py')

file_meta = [(names,os.stat(names)) for names in pyfile]
for name, meta in file_meta:
    print(name,meta.st_size)