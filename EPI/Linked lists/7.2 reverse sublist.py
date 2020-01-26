
class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None


def reverse_sublist(LL,m,n):

    dummy = Node()
    dummy.next = LL
    head = dummy

    for i in range(m-1):
        dummy = dummy.next

    iter = dummy.next
    for i in range(n-m):
        temp = iter.next
        iter.next = temp.next
        temp.next = dummy.next
        dummy.next = temp

    return head.next


l = Node(11)
l.next = Node(3)
l.next.next = Node(5)
l.next.next.next= Node(7)
l.next.next.next.next = Node(2)

res = reverse_sublist(l,1,4)

while res:
    print(res.val)
    res = res.next


