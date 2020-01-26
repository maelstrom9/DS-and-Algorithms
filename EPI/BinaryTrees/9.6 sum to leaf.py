
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def check_sum_to_leaf_match(node,k):
    if not node:
        return False

    rem_sum = k-node.val
    if not node.left and not node.right:
        return rem_sum == 0

    return check_sum_to_leaf_match(node.left,rem_sum) or check_sum_to_leaf_match(node.right,rem_sum)


def possible_match_paths(node,k):
    res = []
    def check_sum_to_leaf_match(node,k,path):
        if not node:
            return False

        rem_sum = k-node.val
        # path.append(node.val) If I directly pass path as global variable that will cause problems in tree stack
        if not node.left and not node.right:
            if rem_sum==0:
                path.append(node.val)
                res.append(path)
                # print(path)

        # check_sum_to_leaf_match(node.left,rem_sum,path.append(node.val)) ## .append returns None, this is prblemeatic as well
        check_sum_to_leaf_match(node.left, rem_sum, path+[node.val])
        # print(path)
        check_sum_to_leaf_match(node.right,rem_sum,path+[node.val])
        # print(path)

    check_sum_to_leaf_match(node,k,[])
    return res
## how to avoid computations once a True is found??


tree = Tree(2)
tree.left = Tree(3)
tree.right = Tree(4)
tree.left.left = Tree(6)
tree.left.right = Tree(6)
tree.right.right = Tree(1)
# tree.left.left.right = Tree(7)
# tree.right.right.left = Tree(8)
# tree.left.left.left.right = Tree(8)

res = check_sum_to_leaf_match(tree,11)
res2 = possible_match_paths(tree,11)

print(res,res2)