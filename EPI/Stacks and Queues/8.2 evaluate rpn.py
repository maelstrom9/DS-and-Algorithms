

def evaluate_rpn(rpn):

    rpn_list = rpn.split(",")
    stack = [] ## basically maintaining two variables always .. O(1) space.

    for c in rpn_list:
        if c.isdigit():
            stack.append(c)
        else:
            r1, r2 = stack.pop(),stack.pop()
            stack.append(eval(int(r1),int(r2),c))
    return stack[0]

## O(n) time complexity..

def eval(a,b,exp):
    if exp=="+":
        return a+b
    elif exp=="-":
        return a-b
    elif exp=="/":
        return a/b
    else:
        return a*b


print(evaluate_rpn("3,4,+,2,x,1,+"))
