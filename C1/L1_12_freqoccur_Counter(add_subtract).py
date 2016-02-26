__author__ = 'Hernan Y.Ke'

from collections import Counter

sample=['cat','boy','dog','cat','cat','boy']
anothersample=['cat','b','c','a','b','b']

word_count = Counter(sample)

print(word_count)

print(word_count['cat'])


# count function can be used in other array
for w in anothersample:       # or word_count.update(anothersample)
    word_count[w]+=1
print(word_count['cat'])

