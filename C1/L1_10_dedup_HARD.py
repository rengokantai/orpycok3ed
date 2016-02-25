__author__ = 'Hernan Y.Ke'

# for only hashable colls
def dedup(items):
    s = set()
    for i in items:
        if i not in s:
            yield i
            s.add(i)


# not hashable colls (i.e. dict)

def dedupnonhash(items, key=None):
    s = set()
    for i in items:
        val = i if key is None else key(i)  # here, we can assign multiple keys. HARD
        if val not in s:
            yield val
            s.add(val)


test = [1, 2, 3, 4, 2, 3]
print(list(dedup(test)))

testdict = [{
                'A': 100,
                'B': 10
            }, {
                'A': 200,
                'B': 10
            }, {
                'A': 100,
                'B': 10
            }]

print(list(dedupnonhash(testdict, key=lambda x: x['A'])))
print(list(dedupnonhash(testdict, key=lambda x: (x['A'], x['B']))))
