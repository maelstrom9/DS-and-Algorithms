
class Tree:
    def __init__(self,val,p):
        self.val = val
        self.left = None
        self.right = None
        self.parent = p

def lca_with_parent(root,n1,n2):

    def get_depth(n):
        d = 0
        while n:
            d += 1
            n = n.parent
        return d

    if not root:
        return -1

    d1,d2 = get_depth(n1),get_depth(n2)

    # d1 = d2 = 0
    # t1,t2 = n1,n2
    #
    # ## Instead of repeating this can be put in a function.
    # while t1:
    #     d1 += 1
    #     t1 = t1.parent
    # while t2:
    #     d2 +=1
    #     t2 = t2.parent
    #
    if d1>d2:
        n1 = n1.parent
        d1 -=1
    elif d2>d1:
        n2 = n2.parent
        d2 -=1

    while n1!=n2:
        n1 = n1.parent
        n2 = n2.parent

    return n1



tree = Tree(2,None)
tree.left = Tree(3,tree)
tree.right = Tree(3,tree)
tree.left.left = Tree(5,tree.left)
tree.right.right = Tree(5,tree.right)
tree.left.left.right = Tree(7,tree.left.left)
tree.right.right.left = Tree(8,tree.right.right)
# tree.left.left.left.right = Tree(8)

res = lca_with_parent(tree,tree.right.right,tree.left.left)

print(res.val)
# print(len(res))