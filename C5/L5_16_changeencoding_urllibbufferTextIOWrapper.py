__author__ = 'Hernan Y.Ke'
import urllib.request
import io,sys,os

print(sys.stdout.encoding)

#change sys.stdout
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='latin-1')
pythonurl = urllib.request.urlopen("http://twitter.com")
f = io.TextIOWrapper(pythonurl,encoding='utf-8')
print(f.read(20))


f = open(os.getcwd()+'\\text2.txt','w')
print(f)
print(f.buffer)
print(f.buffer.raw)

#Now change buffer's encoding

f = io.TextIOWrapper(f.buffer,encoding='latin-1')  #f.buffer, not f
print(f)
print(f.buffer)
print(f.buffer.raw)