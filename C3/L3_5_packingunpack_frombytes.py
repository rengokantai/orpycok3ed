__author__ = 'Hernan Y.Ke'

str1 = b'\xaa\xcc\x12ab' # byte string. memorize this syntax

print(int.from_bytes(str1,'little'))  #little,big

int1=1232342314234234
print(int1.to_bytes(10,'big'))          #compare the syntax   int.from_bytes, 1232.to_bytes


bigint2 = 55**55
print(bigint2.bit_length())

nby,rem = divmod(bigint2.bit_length(),8)
if rem:
    nby+=1
print(bigint2.to_bytes(nby,'little'))