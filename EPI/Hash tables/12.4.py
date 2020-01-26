
class Tree:
    def __init__(self,val,p=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = p

def lca_with_hash_table(n1,n2):

    node_set = set()

    while n1.parent or n2.parent:
        if n1.parent:
            if n1 in node_set:
                return n1
            node_set.add(n1)
            n1 = n1.parent
        if n2.parent:
            if n2 in node_set:
                return n2
            node_set.add(n2)
            n2 = n2.parent

tree = Tree(1)
tree.left = Tree(2,tree)
tree.right= Tree(3,tree)
tree.left.left = Tree(4,tree.left)
tree.left.left.left = Tree(6,tree.left.left)
tree.left.left.left.left = Tree(11,tree.left.left.left)
tree.left.right = Tree(20,tree.left)
tree.left.right.right = Tree(22,tree.left.right)

lca = lca_with_hash_table(tree.left.left.left.left,tree.left.right.right)
print(lca.val)

