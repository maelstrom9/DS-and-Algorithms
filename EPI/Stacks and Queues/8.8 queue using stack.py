

class QueueWithStack:

    def __init__(self):
        self.queue_stack = []
        self.deque_stack = [] ## The key insight is to maintain this stack after popping from queue stack
                        ## to make it easier to process deque..

    def enqueue(self,val):
        self.queue_stack.append(val)

    def dequeue(self):
        if len(self.deque_stack)==0:
            while self.queue_stack:
                self.deque_stack.append(self.queue_stack.pop())

        if len(self.deque_stack)==0:
            raise Exception

        return self.deque_stack.pop()

        # if len(self.queue)==0:
        #     raise IndexError("empty")
        #
        # temp = []
        # while len(self.queue)!=1:
        #     temp.append(self.queue.pop())
        # res = self.queue[0]
        # self.queue = temp[::-1]

        # return res

c = QueueWithStack()
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
print(c.dequeue())
print(c.dequeue())
print(c.dequeue())
c.enqueue(4)
print(c.dequeue())