

class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def inorder_recursion(root):

    res = []

    if root.left:
        res.extend(inorder_recursion(root.left))

    res.append(root.val)

    if root.right:
        res.extend(inorder_recursion(root.right))

    return res


def inorder_loop(root):

    stack = []
    res = []

    cur = root

    while cur or stack:  ## either traverse to the left of the tree, or process stack..
        while cur: ## traverse to left most..
            stack.append(cur)
            cur = cur.left

        ## process stack...
        temp = stack.pop()
        res.append(temp.val)
        if temp.right: ## process right part, ..
            cur = temp.right

    return res


tree = Tree(2)
tree.left = Tree(3)
tree.right = Tree(6)
tree.left.left = Tree(4)
tree.left.right = Tree(5)

print(inorder_recursion(tree))

print(inorder_loop(tree))
