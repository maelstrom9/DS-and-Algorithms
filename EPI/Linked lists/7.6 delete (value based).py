

class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None


## instead of traversing .. this more than o(1)
def delete(node):

    head = node
    while node.next.next:
        node.val = node.next.val
        node = node.next

    node.val = node.next.val
    node.next = node.next.next ## or None
    return head


## copy and delete successor

def delete_efficient(node):
    node.val = node.next.val
    node.next = node.next.next


l1 = Node(11)
l1.next = Node(3)
l1.next.next = Node(5)
l1.next.next.next= Node(7)

res = delete_efficient(l1.next.next)
while l1:
    print(l1.val)
    l1 = l1.next