class Tree:
    def __init__(self,val,n):
        self.val = val
        self.left = None
        self.right = None
        self.parent = n

def inorder_parent(root):

    res = []

    ## 1. Traverse to left most ....
    ## 2. If right child, make that node and repeat 1
    ## 3. If parent towards right, climb up..otherwise stop

    if not root:
        return res

    cur = root

    while cur:
        while cur.left:
            cur = cur.left

        res.append(cur.val)  
        if cur.right:
            cur = cur.right
        else:
            while cur.parent and cur.parent.right==cur:
                cur = cur.parent
                cur.left = None
            cur = cur.parent
            if cur:
                cur.left = None
            # if cur:
            #     res.append(cur.val)
    return res

## O(n) O(n) .... no extra stack space though..


tree = Tree(2,None)
tree.left = Tree(3,tree)
tree.right = Tree(6,tree)
tree.left.left = Tree(4,tree.left)
tree.left.right = Tree(5,tree.left)
tree.left.left.left = Tree(7,tree.left.left)

print(inorder_parent(tree))
