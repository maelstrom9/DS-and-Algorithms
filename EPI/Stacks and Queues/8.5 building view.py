

def views(buildings):

    stack = []

    for b in buildings[::-1]:
        while stack and stack[-1]<= b:
            stack.pop()
        stack.append(b)

    return stack[::-1]


bs = [2,4,5,5,10,2,3,4,11,22,6,5,19,26]

print(views(bs))