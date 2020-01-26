

class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def balanced_tree(root):
    if not root:
        return False

    def check_balance(node):
        ## base case at leaves
        if not node:
            return True,-1

        l,lh = check_balance(node.left)
        if not l:
            return False,0

        r,rh = check_balance(node.right)
        if not r:
            return False,0

        balance = abs(lh-rh)<=1
        height = max(lh,rh)+1

        return balance,height

    return check_balance(root)


tree = Tree(2)
tree.left = Tree(3)
tree.right = Tree(6)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.left.left.left = Tree(7)

print(balanced_tree(tree))

