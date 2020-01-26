
def eval(a,b,exp):
    if exp=="+":
        return a+b
    elif exp=="-":
        return a-b
    elif exp=="/":
        return a/b
    else:
        return a*b


## lambda way of above one
operators = {"+":lambda x,y :x+y,"-":lambda x,y :x-y,
             "x":lambda x,y :x*y,"/":lambda x,y :x/y}

def evaluate_polish(pn):

    pn_list = pn.split(",")
    stack = []

    idx = 0
    while idx<len(pn_list):
        if pn_list[idx] in operators.keys():
            stack.append(pn_list[idx])
        elif stack[-1] not in operators:
            a = stack.pop()
            o = stack.pop()
            stack.append(operators[o](float(a),float(pn_list[idx])))
        else:
            stack.append(pn_list[idx])

        idx+=1
    return stack[0]

print(evaluate_polish("+,+,x,/,2,3,4,2,0"))



