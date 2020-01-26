
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def sum_binary_tree(root):

    if not root:
        return 0

    def inorder_sum(node, s): ## transfer root val below...
        if not node.left and not node.right: ## leaf as base case..return sum
            return node.val+2*s ## height, sum

        ls = rs = 0

        if node.left:
            ls = inorder_sum(node.left,node.val+2*s)
        if node.right:
            rs = inorder_sum(node.right,node.val+2*s)

        return ls+rs

    sum_10 = inorder_sum(root,0)

    return sum_10  ## this has to be converted to binary depending on question.


tree = Tree(1)
tree.left = Tree(0)
tree.right = Tree(0)
tree.left.left = Tree(0)
tree.right.right = Tree(1)
# tree.left.left.right = Tree(7)
# tree.right.right.left = Tree(8)
# tree.left.left.left.right = Tree(8)

res = sum_binary_tree(tree)

print(res)
# print(len(res))



