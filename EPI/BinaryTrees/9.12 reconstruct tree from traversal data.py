

class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def reconstruct(preord,inord):

    ## to save time complexity of the search for the index... everytime..
    inord_dict = {}
    for pos,val in enumerate(inord):
        inord_dict[val] = pos

    def reconstruct_helper(start,end,shift):

        if end<start:
            return None

        # cur = preord[0]
        # print(start,end,shift)
        cur_tree = Tree(preord[start])
        # idx = inord.index(cur)
        idx = inord_dict[preord[start]]
        size = idx - shift

        # if idx>0:
            # left_in = inord[:idx]
            # left_pre = [preord[i] for i in range(1, len(left_in)+1)]
        cur_tree.left = reconstruct_helper(start+1,start+size,shift)
        # if idx+1<=len(inord):
        #     right_in = inord[idx+1:]
        #     right_pre = [preord[i] for i in range(idx + 1, idx + len(right_in) + 1)]
        cur_tree.right = reconstruct_helper(start+1+size,end,shift+size+1)


        return cur_tree

    return reconstruct_helper(0,len(preord)-1,0)


res = reconstruct(["H","B","F","E","A","C","D","G","I"],["F","B","A","E","H","C","D","I","G"])
print(res)




