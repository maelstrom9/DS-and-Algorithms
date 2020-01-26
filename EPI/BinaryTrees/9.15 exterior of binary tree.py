

class Tree:
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None

## Book gave complex recursive sol.. I have done a loop/stack based..with similar time-space complexity..

##1. Inorder but just append the left/right most layer ##
##2. Then only append leaves ###
def get_exteriror_of_tree(root):

    def left_ext(l):
        res = []
        stack = []
        traversed = False
        while l or stack:
            while l:
                if not traversed:
                    res.append(l.val)
                stack.append(l)
                l = l.left

            n = stack.pop()
            if traversed and not n.left and not n.right:
                res.append(n.val)
            traversed = True

            if n.right:
                l = n.right
        return res

    def right_ext(l):
        res = []
        stack = []
        traversed = False
        while l or stack:
            while l:
                if not traversed:
                    res.append(l.val)
                stack.append(l)
                l = l.right

            n = stack.pop()
            if traversed and not n.left and not n.right:
                res.append(n.val)
            traversed = True

            if n.left:
                l = n.left
        return res[::-1]

    return [root.val]+left_ext(root.left)+right_ext(root.right)


tree = Tree(2)
tree.left = Tree(3)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.left.left.left = Tree(6)
tree.left.left.left.right = Tree(7)
tree.right = Tree(8)
tree.right.right = Tree(9)
tree.right.right.left = Tree(14)
tree.right.right.right = Tree(15)


res = get_exteriror_of_tree(tree)

print(res)