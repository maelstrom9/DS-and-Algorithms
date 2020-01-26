
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


## ELEGANT One from book...
def check_symmetric_recursive(root):
    if not root:
        return True

    def check_symmetric(s1,s2):
        ## base case leaf
        if not s1 and not s2:
            return True
        elif s1 or s2:
            return (s1.val == s2.val and check_symmetric(s1.left,s2.right) and check_symmetric(s1.right,s2.left)) ## propogates to top
        return False ## other two cases

    return check_symmetric(root.left,root.right)

def check_symmetric(root):

    stack = [root]
    res = True

    while stack and res:

        stack = [child for node in stack for child in [node.left,node.right] if child]

        if len(stack)%2==1:
            res = False

        l = 0
        r = len(stack)-1
        while l<r and res:
            if stack[l].val != stack[r].val:
                res = False
            l+=1
            r-=1
    return res


tree = Tree(2)
tree.left = Tree(3)
tree.right = Tree(3)
tree.left.left = Tree(5)
tree.right.right = Tree(5)
tree.left.left.right = Tree(7)
tree.right.right.left = Tree(8)
# tree.left.left.left.right = Tree(8)

res = check_symmetric_recursive(tree)

print(res)



