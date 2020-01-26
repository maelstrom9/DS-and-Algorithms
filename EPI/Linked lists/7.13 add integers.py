
class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def add_ll_integers(l1,l2):

    head = l1

    c = 0
    while l1.next and l2.next:
        v1 = l1.val
        v2 = l2.val
        c, v = divmod(v1+v2+c,10)

        l1.val = v

        l1 = l1.next
        l2 = l2.next

    l1.val = l2.val + l1.val
    # print(l1.val)
    if l2.next!=None:
        l1.next = l2.next

    ## appending list has elements left over..
    while l1.next:
        c, v = divmod(l1.val+ c, 10)
        l1.val = v
        l1 = l1.next

    c,v = divmod(l1.val+c,10)
    l1.val = v
    if c!=0:
        l1.next = Node(c)

    return head

a = [2,2,1]

l1 = Node(3)
dummy = l1
for i in a:
    dummy.next = Node(i)
    dummy = dummy.next

b = [2,2,1]

l2 = Node(9)
dumm = l2
for i in b:
    dumm.next = Node(i)
    dumm = dumm.next

res = add_ll_integers(l2,l1)
while res:
    print(res.val)
    res = res.next