
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def form_ll_with_leaves(root):

    stack = []
    head = Node(None)
    dummy = head

    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        node = stack.pop()
        if not node.left and not node.right:
            dummy.next = Node(node.val)
            dummy = dummy.next

        if node.right:
            cur = node.right

    return head.next


tree = Tree(2)
tree.left = Tree(3)
tree.right = Tree(6)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.left.left.left = Tree(7)

res = form_ll_with_leaves(tree)
print(1)


