

class Tree:

    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None

## O(n) and O(n) complex rules, by tracking the parent in a stack..
def recon_pre_markers(premark_list):

    parents_stack = [None]
    i = 0
    ## set root
    node = Tree(premark_list[i])
    parents_stack.append(node)
    while node and i<len(premark_list):
        ## traverse left
        while  i<len(premark_list) and premark_list[i]!=None:
            node.left = Tree(premark_list[i])
            node = node.left
            parents_stack.append(node)
            i+=1

        i+=1 ## skip the left null

        ## skip the nodes with right nulls
        while  i<len(premark_list) and premark_list[i]==None:
            node = parents_stack.pop()
            i+=1

        ## traverse back if coming from right child
        while len(parents_stack)>1 and parents_stack[-1].right == node:
            node = parents_stack.pop()

        ## set the leftmost right as the new node and repeat..
        if i<len(premark_list):
            node = Tree(premark_list[i])
            parents_stack[-1].right = node
            parents_stack.append(node)
            i += 1

    return node


## From the hint
## O(1) space and O(n) solution
def recon_pre_markers_right_to_left(pre_mark_list):
    stack = []  ## max 2-3
    for i in reversed(pre_mark_list):
        if i==None:
            stack.append(i)
        else:
            node = Tree(i)
            node.left = stack.pop()
            node.right = stack.pop()
            stack.append(node)
    return stack[0]

## book recursive solution.. O(n) time, O(h) space from function call stack
def reconstruct_preorder(preorder):
    def reconstruct_preorder_helper(preorder_iter):
        key = next(preorder_iter)
        if key is None:
            return None
        left = reconstruct_preorder_helper(preorder_iter)
        right = reconstruct_preorder_helper(preorder_iter)
        cur_tree = Tree(key)
        cur_tree.left = left
        cur_tree.right = right
        return cur_tree
    return reconstruct_preorder_helper(iter(preorder))

res = recon_pre_markers(["H","B","F",None,None,"E","A",None,None,None,"C",None,"D",None,"G","I",None,None,None])

res2 = recon_pre_markers_right_to_left(["H","B","F",None,None,"E","A",None,None,None,"C",None,"D",None,"G","I",None,None,None])
print(res)

