
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


## added variant alternating left to right also..
def bfs_queue(tree):

    queue = [tree]

    ltor = 1 ## left to right
    res = []

    while queue:
        if ltor:
            res.append([node.val for node in queue])
        else:
            res.append([node.val for node in reversed(queue)])
        # queue = [child for node in queue for child in [node.left,node.right] if child]
        temp = [] ## basically popping everything.
        for node in queue:
            for child in [node.left,node.right]:
                if child:
                    temp.append(child)
        queue = temp

        ltor ^= 1
    return res


tree = Tree(5)
tree.left = Tree(4)
tree.right = Tree(6)
tree.left.left = Tree(5)
tree.left.left.left = Tree(9)
tree.left.left.right = Tree(10)

print(bfs_queue(tree))