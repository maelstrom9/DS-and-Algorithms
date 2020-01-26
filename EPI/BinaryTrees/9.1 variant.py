

class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

## max size of the complete binary tree

def get_max_size(root):
    if not root:
        return 0

    def check_balance(node):
        if not node:
            return True,-1, 0 ## balance, height and size

        lb, lh, ls = check_balance(node.left)
        rb, rh, rs = check_balance(node.right)

        balance = abs(lh-rh)<=1
        height = max(lh,rh)+1
        # size = ls+rs
        if lb and rb and balance: ## both balanced..
            size = ls+rs+1
            return balance,height,size
        else:  ## when left tree or right tree or both is not balanced...
            return False,0,max(ls,rs)

    return check_balance(root)


tree = Tree(2)
tree.left = Tree(3)
tree.right = Tree(6)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.left.left.left = Tree(7)
tree.left.left.left.left = Tree(7)
tree.left.left.left.right = Tree(8)

print(get_max_size(tree))