
class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def list_pivot(ll,pivot):

    less,equal,more = Node(),Node(),Node()
    l,e,m = less,equal,more

    while ll:
        if ll.val<pivot:
            l.next = ll
            l = l.next
        elif ll.val==pivot:
            e.next = ll
            e = e.next
        else:
            m.next = ll
            m = m.next
        ll = ll.next

    m.next = None
    e.next = more.next
    l.next = equal.next

    return less.next


a = [2,2,11,7,5,11]

l1 = Node(3)
dummy = l1
for i in a:
    dummy.next = Node(i)
    dummy = dummy.next

res = list_pivot(l1,7)
while res:
    print(res.val)
    res = res.next
