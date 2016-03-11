__author__ = 'Hernan Y.Ke'

def re(*values,keyword=None):
    m = min(values)
    if keyword is not None:
        m = keyword if keyword>m else m
    return m

print(re(1,2,-1))
print(re(1,2,-1,keyword=4))
