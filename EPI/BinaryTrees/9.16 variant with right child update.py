

class Tree:
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None


## O(n), O(leaves) solution..
def update_right_field(root):

    stack = [root]

    while stack:

        temp = [child for node in stack for child in [node.left,node.right] if child]

        for i in range(len(stack)):
            if i == len(stack)-1:
                stack[i].right = None
            else:
                stack[i].right = stack[i+1]

        stack = temp

    return root


tree = Tree(2)
tree.right = Tree(8)
tree.left = Tree(3)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.right.right = Tree(9)
tree.right.left = Tree(10)


res = update_right_field(tree)

print(1)