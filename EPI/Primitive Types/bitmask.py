## First a binary no. can be represented starting with '0b'

## Ex: "0b1000" = 8

def check_bit(integer,index):
    '''A function to
    check if a integer(binary format)
    has 1 at a specified index'''
    mask = 1
    for i in range(index-1):
        mask<<=1
    print(bin(mask))
    # print(type(mask))

    if mask&integer>0:
        return "yes"
    else:
        return "no"

print(check_bit(0b111001,2))