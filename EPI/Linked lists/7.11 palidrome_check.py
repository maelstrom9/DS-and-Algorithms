
class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None


def palidrome_check(ll):

    # get the midpoint
    slow = fast = ll
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    first, second = ll, reverse(slow)
    while second:
        if first.val!=second.val:
            return False
        first = first.next
        second = second.next

    return True


## 0->1->2->3->

def reverse(ll):
    head = Node()
    head.next = ll
    dummy = head

    iter = dummy.next
    while iter.next:
        temp = iter.next

        iter.next = temp.next
        temp.next = dummy.next
        dummy.next = temp

    return head.next

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
l1.next.next.next= Node(2)
l1.next.next.next.next= Node(1)
l1.next.next.next.next.next= Node(6)
l1.next.next.next.next.next.next= Node(7)

res = palidrome_check(l1)

print(res)