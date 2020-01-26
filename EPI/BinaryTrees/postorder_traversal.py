
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def postorder_recursion(root):

    temp = []

    if root.left:
        temp.extend(postorder_recursion(root.left))

    if root.right:
        temp.extend(postorder_recursion(root.right))

    temp.append(root.val)

    return temp


def postorder_loop(root): ## reverse inorder..not straight reverse but..

    stack = [root]
    res = []

    while stack:
        cur = stack.pop()
        res.append(cur.val)

        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)

    return res[::-1]


tree = Tree(2)
tree.left = Tree(3)
tree.right = Tree(6)
tree.left.left = Tree(4)
tree.left.right = Tree(5)

assert postorder_recursion(tree)==[4,5,3,6,2]

print(postorder_loop(tree))