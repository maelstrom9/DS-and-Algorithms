

def  base_conversion(str_A,b1,b2):

    # conv_dict = {}
    # for i in range(10):
    #     conv_dict[i] = i


    sign = False
    num_val = 0
    for i in str_A:
        if i=="-":
            sign = True
        else:
            num_val *= b1
            num_val += ord(i)-ord("0")

    res = []
    if num_val==0:
        return "0"

    while num_val:
        num_val,rem = divmod(num_val,b2)
        if rem>=10:
            res.append(chr(ord("A")+rem-10))
        else:
            res.append(chr(ord("0")+rem))



    if sign:
        res.append("-")

    return "".join(reversed(res))

print(base_conversion("615",7,13))