
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def lca(root,node1,node2):

    if not root:
        return root

    res = []

    def check_lca(node,node1,node2):
        ## if None case is taken as base case, produces cleaner code..
        if not node.left and not node.right: ## Leaf... base case
            return (False or node==node1,False or node==node2) ## m,n

        l = (False,False)
        r = (False,False)

        if node.left:
            l = check_lca(node.left,node1,node2)
            if l[0] and l[1]:
                return l
        if node.right:
            r = check_lca(node.right,node1,node2)
            if r[0] and r[1]:
                return r

        temp =  (l[0] or r[0] or node==node1,l[1] or r[1] or node==node2)
        if temp[0] and temp[1]:
            res.append(node) ## this variable is created in fucntion space so it doenst work.. but if this is global list, then append works for ex
            # node1=None
            # node2=None
        return temp

    check_lca(root,node1,node2)
    return res


tree = Tree(2)
tree.left = Tree(3)
tree.right = Tree(3)
tree.left.left = Tree(5)
tree.right.right = Tree(5)
tree.left.left.right = Tree(7)
tree.right.right.left = Tree(8)
# tree.left.left.left.right = Tree(8)

res = lca(tree,tree.left.left.right,tree.left.left)

print(res[0].val)
print(len(res))

