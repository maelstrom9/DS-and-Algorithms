




def well_formed(exp):

    comps = {"{":"}","(":")","[":"]"}
    stack = []

    for c in exp:
        if c in comps:
            stack.append(c)
        elif not stack or comps[stack.pop()]!=c:
            return False

    return len(stack)==0

print(well_formed("{[()]}{}"))  ## all the elements need not be checked... first unmatch can result in false..

