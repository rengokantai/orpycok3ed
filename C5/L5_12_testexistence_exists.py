__author__ = 'Hernan Y.Ke'
import os
import time
print(os.path.exists(os.path.abspath(os.getcwd())))

#getsize getmtime

#isdir isfile realpath

print(os.path.getmtime((os.path.abspath(os.getcwd()))))
print(time.ctime(os.path.getmtime((os.path.abspath(os.getcwd())))))      #time.ctime