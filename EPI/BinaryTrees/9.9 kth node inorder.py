




class Tree:
    def __init__(self,val,n):
        self.val = val
        self.left = None
        self.right = None
        self.nn = n

def kth_node_inorder(root,k):


    ## better way
    while root:
        left_size = root.left.nn if root.left else 0 ## else size == 0
        if k-1 == left_size:
            return root
        elif k>left_size+1:
            root = root.right
            k -= left_size+1
        else:
            root = root.left

    # return None

    # if not root:
    #     return root
    #
    # if not root.left and not root.right and root.nn==k-1:
    #     return root
    # elif root.left and root.left.nn+2 == k:
    #     return root
    # elif root.left and k<=root.left.nn+1:
    #     return kth_node_inorder(root.left,k)
    # elif root.left and root.right and k>root.left.nn+1:
    #     return kth_node_inorder(root.right,k-root.left.nn-2)
    # elif not root.left and root.right:
    #     return kth_node_inorder(root.right,k-1)
    # elif not root.right and root.left:
    #     return kth_node_inorder(root.left,k)


tree = Tree(2,6)
tree.left = Tree(3,4)
tree.right = Tree(6,1)
tree.left.left = Tree(4,2)
tree.left.right = Tree(5,1)
tree.left.left.left = Tree(7,1)


## [7,4,3,5,2,6]
for i in range(1,8):
    print(kth_node_inorder(tree,i).val)
