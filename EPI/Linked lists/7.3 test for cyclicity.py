
class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def test_cyclicity(head):
    if not head:
        return False,-1

    slow = fast = head
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        ## for length traverse from the meet point to meet it again

        ## this is to find start node, kc = x+y...  (k-1)c+z = x ... slow takes x steps..y
        ## takes some cycles plus z making it meet at the start point of the cycle..
        if slow==fast:
            slow = head
            while slow!=fast:
                slow = slow.next
                fast = fast.next
            return True,slow

    return False,-1,0

l = Node(11)
l.next = Node(3)
l.next.next = Node(5)
l.next.next.next= Node(7)
l.next.next.next.next = Node(2)
l.next.next.next.next.next= Node(8)
l.next.next.next.next.next.next = l.next.next

_,res = test_cyclicity(l)

print(res.val)