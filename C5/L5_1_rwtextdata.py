__author__ = 'Hernan Y.Ke'

#append to the end of existing file, using mode `at`

# read as single string
with open('','rt') as f:
    data = f.read()

#iterate over lines
with open('','rt',newline='',encoding='ascii',errors='ignore') as f: #possible errors value: ignore,replace
    for line in f:
        pass

#write chunks
with open('','wt') as f:
    f.write()
    f.write()

#print chunks
with open('','wt') as f:
    print('',file=f)        # file keyword
    print('',file=f)

