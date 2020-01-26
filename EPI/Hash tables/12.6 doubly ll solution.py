

class DoublyLinkedListNode:

    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def insert_after(self,value):

        node = DoublyLinkedListNode(value)
        node.prev = self.tail

        if self.tail:
            self.tail.next = node
        else:
            self.head = node ## when both are none, both become head and tail
        self.tail = node
        self._size +=1

    ## remove a node
    def remove(self,node):
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        node.next = node.prev = None  ## Explicit.?

        self._size -=1


def find_smallest_sub_arr(arr,sub):

    dll = DoublyLinkedList()
    hash_table = {s:None for s in sub} ## intersting dictionary comprehension
    g_dist = float('inf') ## Instead,,,, indices can also be maintained here... good!!!!

    for idx,word in enumerate(arr):
        if word in sub:
            if hash_table[word] is not None:
                dll.remove(hash_table[word])
            dll.insert_after(idx)
            hash_table[word] = dll.tail ## because its always tail.

        if len(dll)==len(sub):
            ## update distance
            dist = dll.tail.val - dll.head.val
            g_dist = min(dist,g_dist)

    return g_dist

c = ["I","a","up","ok","r", "a","the","ar","s","up","a","a"]
sub2 = ["up","the","a"]

res = find_smallest_sub_arr(c,sub2)
print(res)





