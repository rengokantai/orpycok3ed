__author__ = 'Hernan Y.Ke'
from tempfile import TemporaryDirectory, TemporaryFile,NamedTemporaryFile

with TemporaryFile('w+t',encoding='utf-8') as f: #or f = TemporaryFile('w+t')
    f.write('test')
    f.seek(0)
    print(f.read())


#named
with NamedTemporaryFile('w+t',delete=True) as f:
    print(f.name)

# tempfile.mkstemp()
# tmpfile.mkdtemp()
# tmpfile.gettempdir()