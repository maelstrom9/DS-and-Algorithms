

class Tree:
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None


## iter method from book  O(n) and O(stack=h) including None..
def recon_postorder(post_ord_list):
    # post_ord_list = post_ord_list[::-1]
    def helper(it):

        val = next(it) ## first next gives first element of iter..
        if val == None: ## base case
            return None

        tree = Tree(val)
        tree.right = helper(it)
        tree.left = helper(it)
        return tree
    return helper(reversed(post_ord_list))


## stack based one --mine
def recon_stack_post(post_ord_list):
    stack = []
    for i in post_ord_list:
        if i==None:
            stack.append(i)
        else:
            tree = Tree(i)
            tree.right = stack.pop()
            tree.left = stack.pop()
            stack.append(tree)
    return tree


res = recon_postorder([None,None,"F",None,None,"A",None,"E","B",None,None,None,None,"I",None,"G","D","C","H"])
res2 = recon_stack_post([None,None,"F",None,None,"A",None,"E","B",None,None,None,None,"I",None,"G","D","C","H"])
print(res)