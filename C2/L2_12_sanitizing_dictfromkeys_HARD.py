__author__ = 'Hernan Y.Ke'
import unicodedata
import sys

map={ord('\t'):'tab'}

oldstr ='one\ttwo'
print(oldstr.translate(map))

cmbchar = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c))) #convert all combining char to none
# must be str.default is int.
print(cmbchar)

str2 = 'n\u0303o'

print(str2.translate(cmbchar))

#list all ascii
digimap = {c:ord('0')+unicodedata.digit(chr(c))for c in range(sys.maxunicode)if unicodedata.category(chr(c))=='Nd'}
x='\u0662'
print(x.translate(digimap))


#this is a hack.

print(str2.encode('ascii','ignore').decode('ascii'))