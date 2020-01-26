### fuck I dont need to put L1 into L2 literally!!
### I can create a place holder to do that, which makes the code much simpler..

### Here we are just playing with the space unlike
### lists/arrays so time complexity reamins O(1)...

class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def merge_two_ll(L1,L2):

    head = merge = Node()

    while L1 and L2:
        if L1.val<L2.val:
            merge.next = L1
            L1 = L1.next
        else:
            merge.next = L2
            L2 = L2.next
        merge = merge.next


    merge.next = L1 or L2 ## elegant one..

    return head.next ## as there is dummy node..

L1 = Node(2)
L1.next = Node(5)
L1.next.next = Node(7)

L2 = Node(3)
L2.next = Node(4)
L2.next.next = Node(4)

merge = merge_two_ll(L1,L2)
while merge:
    print(merge.val)
    merge = merge.next
