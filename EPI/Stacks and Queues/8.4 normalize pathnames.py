



def normalize(path):

    path_list = path.split("/")
    stack = []

    for c in path_list:
        if c=="" or c==".":
            continue
        elif len(stack)==0 or c!="..":
            stack.append(c)
        elif c == "..":
            stack.pop()

    return "/".join(stack)


print(normalize("scripts//./../scripts/awkscripts/././"))
print(normalize("/usr/lib/../bin/gcc"))

## Special case / has also to be handled above...