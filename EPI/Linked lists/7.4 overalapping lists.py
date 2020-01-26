
class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None


## checks for overlap,..
## returns bool overlap? and first overlap node..

def overlap(l1,l2):

    h1, h2 = l1, l2
    ## first l1 and l2 are to be checked as well.. assuming they are not None
    m = 1
    while l1.next:
        l1 = l1.next
        m += 1

    n = 1
    while l2.next:
        l2 = l2.next
        n += 1

    h = None
    if l1==l2:
        dif = abs(m-n)
        if m>n:
            h = h1
            l = h2
        else:
            h = h2
            l = h1
        for _ in range(dif):
            h = h.next
        while h!=l:
            h = h.next
            l = l.next

    return l1==l2, h

l1 = Node(11)
l1.next = Node(3)
l1.next.next = Node(5)
l1.next.next.next= Node(7)

l2 = Node(13)
l2.next = l1.next.next

b,res = overlap(l1,l2)

if res!=None:
    print(b,res.val)
else:
    print(b,res)

