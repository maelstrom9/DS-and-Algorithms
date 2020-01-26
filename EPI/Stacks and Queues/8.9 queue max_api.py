
from collections import deque


## this deque is a doubly linked list making push/pop O(1) unlink arrays/lists..
## this should be probably discussed in interviews...

class QueueWithMAxAPI:

    def __init__(self):
        self.queue = deque()
        self.max = deque() ## make it like a queue..

    def enqueue(self,val):
        self.queue.append(val)
        while self.max and self.max[-1]<val:
            self.max.popleft()
        self.max.append(val)

    def dequeue(self):
        if len(self.queue)==0:
            raise Exception
        temp = self.queue.popleft()
        if temp==self.max[0]:
            self.max.popleft()
        return temp

    def get_max(self):
        if self.max:
            return self.max[0]
        raise Exception


q = QueueWithMAxAPI()

q.enqueue(10)
print(q.get_max())

q.enqueue(10)
print(q.get_max())

q.enqueue(12)
print(q.get_max())

q.dequeue()
print(q.get_max())

q.dequeue()
print(q.get_max())

q.enqueue(9)
print(q.get_max())

q.dequeue()
print(q.get_max())