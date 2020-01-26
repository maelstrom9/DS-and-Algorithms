
class Tree:
    def __init__(self,val,n):
        self.val = val
        self.left = None
        self.right = None
        self.parent = n

def succesor_inorder(root,node):

    ## 2. when there is right children.... return the left most leaf of the right subtree...
    ## 3. when there is no right children... search till root... and return the first encountered left turn node..else None
    ## 1. If there is left children immedigate return that...

    if not root or node==root:
        return None

    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    else:
        # while node.parent and node.parent.right == node:
            # node = node.parent
        parent = node.parent
        while parent: ## until parent becomes None
            if parent.left and parent.left == node:
                return parent
            else:
                node = parent
                parent = node.parent
        return parent


tree = Tree(2,None)
tree.left = Tree(3,tree)
tree.right = Tree(6,tree)
tree.left.left = Tree(4,tree.left)
tree.left.right = Tree(5,tree.left)
tree.left.left.left = Tree(7,tree.left.left)

print(succesor_inorder(tree,tree.left.right).val)

## O(h) time, O(1) space..


