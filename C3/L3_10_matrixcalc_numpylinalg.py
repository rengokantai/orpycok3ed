__author__ = 'Hernan Y.Ke'
import numpy as np
import numpy.linalg

m = np.matrix([[1,2,3],[3,2,1],[1,3,5]])

print(m.T,m.I,numpy.linalg.det(m),numpy.linalg.eigvals(m))

v=np.matrix([[3],[5],[2]])

#solve mx=v
print('---')
x=numpy.linalg.solve(m,v)
print(x)