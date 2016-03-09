__author__ = 'Hernan Y.Ke'
import unicodedata

str1 = '\u00f1o'
str2 = 'n\u0303o'

print(len(str1))
print(len(str2))

# possible values: NFC(composed) NFD(decomposed)
print(unicodedata.normalize('NFD',str1))
print(unicodedata.normalize('NFD',str2))
print(unicodedata.normalize('NFD',str1)==unicodedata.normalize('NFD',str2))
print(ascii(unicodedata.normalize('NFD',str2)))
print(ascii(unicodedata.normalize('NFD',str1)))

print('------')

print(unicodedata.normalize('NFC',str1))
print(unicodedata.normalize('NFC',str2))
print(unicodedata.normalize('NFC',str1)==unicodedata.normalize('NFC',str2))
print(ascii(unicodedata.normalize('NFC',str2)))
print(ascii(unicodedata.normalize('NFC',str1)))


print(unicodedata.normalize('NFC',str1)==unicodedata.normalize('NFD',str2))  #not true

# NFKC,NFKD for single charactors

#filter non-latin letters, ascii codes
print(''.join(c for c in str2 if not unicodedata.combining(c)))