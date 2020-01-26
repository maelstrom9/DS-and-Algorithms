
def int_to_string(no):

    ## explicit 0 condition
    if no==0:
        return "0"

    sign = False
    if no<0:
        sign = True

    no = abs(no)
    res = [] ## maintaining an array is better than directly working on strings.

    while no:
        no,r = divmod(no,10)
        res.append(chr(ord('0')+r)) ## key

    if sign:
        res+="-"
    return ''.join(reversed(res))

print(ord("0"))
print(chr(48))
print(int_to_string(-123))


def string_to_int(s):

    sign = False
    res = 0
    for i in s:
        if i=="-":
            sign = True
        else:
            res *= 10
            res += ord(i)-ord("0") ##key
    if sign:
        res = -res
    return res


print(string_to_int("-42242"))