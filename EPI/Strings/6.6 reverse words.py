

def reverse_words(s):
    arr = list(s)
    s = 0
    # e = 0

    for idx in range(len(arr)):
        if arr[idx]==" ":
            arr = rev(arr,s,idx-1)
            # print(arr)
            s = idx+1
        # e += 1
    if arr[len(arr)-1]!=" ": ## if last in not space, edge/special case..
        arr = rev(arr,s,len(arr)-1)
    return "".join(reversed(arr)) ## o(n)


def rev(arr,s,e):
    # for i in range(s,1+(s+e-1)//2):
    while s<e:
        arr[s],arr[e] = arr[e],arr[s]
        s += 1
        e -= 1
    return arr

print(reverse_words("bobas ;;as    is clever"))


# s = "abc"
# s[0] ="a"
# print(s)

# s = [1,2,3]
# s.reverse()
# print(s) ## reverse inplace..
# s = reversed(s)  ## returns iterator
# # s.reverse()
# print(s)
