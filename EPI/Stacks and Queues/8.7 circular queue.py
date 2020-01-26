


class CircularQueue:

    scale = 2

    def __init__(self,cap):
        self.queue = [None]*cap
        self.head = 0
        self.tail = 0
        self.n = 0
        # self.cap = cap

    def enqueue(self,val):
        if self.n == len(self.queue):
            # self.queue.append(val) ## this is a mistake.. because of positions of head and tail, deque can pick wrong head.
            self.queue = self.queue[self.head:]+self.queue[:self.head]
            self.head, self.tail = 0, len(self.queue)
            self.queue += [None]*len(self.queue)*CircularQueue.scale
            # self.n += 1
            # self.tail += 1
            # self.cap +=1
        # else:
        self.queue[self.tail] = val
        self.tail = (self.tail+1)%len(self.queue)
        # self.tail += 1
        self.n+=1

    def deque(self):
        if self.n==0:
            raise IndexError("EmptyQueue")
        temp = self.queue[self.head]
        # self.queue[self.head] = None ## do i need this?--nope/depends..
        # self.head += 1
        self.head = (self.head+1)%len(self.queue)
        self.n -=1
        return temp

    def no_of_elem(self):
        return self.n


c = CircularQueue(3)

c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
print(c.queue)
print(c.no_of_elem())
c.deque()
c.deque()
c.enqueue(4)
c.enqueue(5)
c.enqueue(6)
print(c.no_of_elem())
print(c.queue)
print(c.deque())
print(c.no_of_elem())

