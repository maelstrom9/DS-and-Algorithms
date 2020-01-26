


class Heap:

    def __init__(self):
        self.h = [None]


    def add(self,v):
        self.h.append(v)

        child = len(self.h)-1
        parent = child//2
        while parent:
            if self.h[parent]>self.h[child]:
                self.h[parent], self.h[child] = self.h[child], self.h[parent]
                child = parent
                parent = parent//2
            else:
                break

heap = Heap()

heap.add(1)
heap.add(4)
heap.add(2)
heap.add(11)
heap.add(112)
heap.add(14)
heap.add(9)
heap.add(3)
heap.add(2)

print(heap.h)