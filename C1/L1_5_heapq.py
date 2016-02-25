__author__ = 'Hernan Y.Ke'
import heapq


class PriQueue:
    def __init__(self):
        self._index = 0
        self._queue = []

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heapq.heappop(array) will pop with `min` priority.
        return heapq.heappop(self._queue)[-1]   #return last attribute which is item name.



class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{!r}".format(self.name)


q = PriQueue()
q.push(Item('kk'), 10)
q.push(Item('zz'), 20)
q.push(Item('aa'), 1)

print(q.pop())
print(q.pop())
print(q.pop())
