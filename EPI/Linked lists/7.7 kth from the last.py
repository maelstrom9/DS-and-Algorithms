


class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None


## 1 2 3 4 5 6 ..


def kth_from_last(ll,k):

    dummy = head = Node()
    head.next = ll

    for _ in range(k):
        head = head.next

    dummy2 = dummy
    # print(dummy2.val)
    while head.next:
        # print("")
        head = head.next
        dummy2 = dummy2.next

    dummy2.next = dummy2.next.next
    # print(dummy2.next.val)

    return dummy.next

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
l1.next.next.next= Node(4)
l1.next.next.next.next= Node(5)
l1.next.next.next.next.next= Node(6)

res = kth_from_last(l1,3)
while res:
    print(res.val)
    res = res.next

