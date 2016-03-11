__author__ = 'Hernan Y.Ke'
import binascii,base64
st = b'ke'
hexst =binascii.b2a_hex(st)
print(hexst)
hexst =base64.b16encode(st)
print(hexst)
# decode
print((hexst.decode('ascii')))

st = binascii.a2b_hex(hexst)
print(st)
st =base64.b16decode(hexst)
print(st)





