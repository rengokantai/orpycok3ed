__author__ = 'Hernan Y.Ke'
import pickle,os
data={'a':3}
f = open(os.getcwd()+'\\text2.txt','wb')
pickle.dump(data,f)             #syntax: dump(data,filename)

f = open(os.getcwd()+'\\text2.txt','rb')
print(pickle.load(f))

# for string, use pickle.dumps and pickle.loads


