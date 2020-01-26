

class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def reconstruct(inord,postord):

    inord_dict = {v:i for i,v in enumerate(inord)}
    postord = postord[::-1]

    def helper(start,end,shift):

        if start>end:
            return None

        cur_val = postord[start]
        cur_tree = Tree(cur_val)
        idx = inord_dict[cur_val]
        # size = len(postord)-idx-1-shift
        size = shift - idx  ## size of the right side elements...

        cur_tree.left = helper(start+size+1,end,idx-1) ## idx-1 is the remaining size on left side..
        cur_tree.right = helper(start+1,start+size,shift)

        return cur_tree

    return helper(0,len(postord)-1,len(postord)-1)

inord = "EDFBHACRKS"
postord = "EFDHBRSKCA"

res = reconstruct(list(inord),list(postord))

print(res)

