

class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def cyclic_shift(ll,k):

    if k==1:
        return ll

    # dummy = Node()
    # dummy.next = ll
    head  = ll

    for _ in range(k-2):
        head = head.next

    last = head

    first= head.next
    while head.next:
        head = head.next

    head.next = ll
    last.next = None

    return first


l1 = Node(2)
l1.next = Node(3)
l1.next.next = Node(5)
l1.next.next.next= Node(3)
l1.next.next.next.next= Node(2)
# l1.next.next.next.next.next= Node(6)

res = cyclic_shift(l1,1)
while res:
    print(res.val)
    res = res.next



