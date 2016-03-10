__author__ = 'Hernan Y.Ke'
import itertools


def count(x):
    while True:
        yield x
        x += 1


ct = count(0)  # base case
for x in itertools.islice(ct, 5, 10):  # memorize this syntax
    print(x)

