


class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def remove_duplicates_from_ll(ll):
    if not ll:
        return ll

    # head = ll

    prev = ll
    cur = ll
    while cur:
        if cur.val == prev.val:
            cur = cur.next
            ## handling None case
            if cur==None:
                prev.next = cur
        else:
            prev.next = cur
            prev = cur
            cur = cur.next
    return ll



l1 = Node(1)
l1.next = Node(1)
l1.next.next = Node(2)
l1.next.next.next= Node(2)
l1.next.next.next.next= Node(2)
l1.next.next.next.next.next= Node(6)

res = remove_duplicates_from_ll(l1)
while res:
    print(res.val)
    res = res.next
