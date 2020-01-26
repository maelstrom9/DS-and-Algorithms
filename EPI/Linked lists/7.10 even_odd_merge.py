
class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None


## 0 1 2 3
def even_odd_merge(ll):

    odd = Node()
    even = Node()

    o = odd
    e = even

    head = ll
    c = 0
    while head:
        if c%2==0:
            e.next = head
            e = e.next
        else:
            o.next = head
            o = o.next
        c+=1
        head = head.next

    o.next = None
    e.next = odd.next
    return even.next



l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
l1.next.next.next= Node(4)
l1.next.next.next.next= Node(5)
l1.next.next.next.next.next= Node(6)

res = even_odd_merge(l1)
while res:
    print(res.val)
    res = res.next