

class Tree:
    def __init__(self,v,l_next=None):
        self.val = v
        self.left = None
        self.right = None
        self.l_next = l_next

def set_level_next_perfect_binary_tree(root):

    queue = [root]

    while queue:

        temp = []

        for idx in range(len(queue)):
            if queue[idx].left: ## perfect binary tree
                temp += [queue[idx].left,queue[idx].right]
            if idx>=1:
                queue[idx-1].l_next = queue[idx]
        queue = temp

    return root


## book
## key idea if left child--> parent.next
##          if right child-->parent.next.left

def update_next(root):
    def helper(node):
        while node and node.left:
            node.left.l_next = node.right

            node.right.l_next = node.l_next and node.l_next.left
            node = node.left
    helper(root)
    # root = root.left

tree = Tree(2)
tree.right = Tree(8)
tree.left = Tree(3)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.right.right = Tree(9)
tree.right.left = Tree(10)

# res = set_level_next_perfect_binary_tree(tree)
update_next(tree)
print(1)

x = 2
y = 3
z = x and y
print(y)