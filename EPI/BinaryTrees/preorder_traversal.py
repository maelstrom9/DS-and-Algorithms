
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def preorder_recursion(root,res=[]):

    ## this will trigger only when root is None..
    if not root:
        return []

    res.append(root.val)

    if root.left:
        preorder_recursion(root.left,res)

    if root.right:
        preorder_recursion(root.right,res)

    return res


def preorder_loop(root):

    stack = [root]
    res = []

    while stack:

        cur = stack.pop()
        res.append(cur.val)

        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res



tree = Tree(2)
tree.left = Tree(3)
tree.right = Tree(6)
tree.left.left = Tree(4)
tree.left.right = Tree(5)

print(preorder_recursion(tree,[]))