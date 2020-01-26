

class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def k_balanced(root,k):
    if not root:
        return -1

    nodes = []

    def check_balance(node):
        if not node:
            return 0 ## size

        ls = check_balance(node.left)
        rs = check_balance(node.right)

        if abs(ls-rs)>k:
            nodes.append(node)

        return ls+rs+1

    check_balance(root)

    return nodes



tree = Tree(2)
tree.left = Tree(3)
tree.right = Tree(6)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.left.left.left = Tree(7)
tree.left.left.left.left = Tree(7)
tree.left.left.left.right = Tree(8)

res = k_balanced(tree,2)
for i in res:
    print(i.val)