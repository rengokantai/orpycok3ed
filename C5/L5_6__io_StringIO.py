__author__ = 'Hernan Y.Ke'
import io
s = io.StringIO()
print(s.write('test\n'))

print(s.getvalue())
print(s.read(5))

b = io.BytesIO()
print(b.write(b'test\n'))
print(b.getvalue())