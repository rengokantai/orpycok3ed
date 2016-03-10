__author__ = 'Hernan Y.Ke'

def showlist(list):
    x = True
    while x is not None:
        x = next(list, None)  # return None to prevent stopiteration error
        print(x)


showlist(iter([1,3,4,5,7]))
