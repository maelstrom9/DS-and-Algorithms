

## bits &= bits-1

def clear_lower_most_set_bit(integer):
    print(bin(integer),bin(integer-1))
    return integer&(integer-1)

print(clear_lower_most_set_bit(10))


## But how to get the index?
## loop over the bits and check?

def get_index(integer):
    index = 0
    n = 1
    if integer==0:
        return "NA"
    while True:
        if integer&n>0:
            return index
        else:
            index+=1
            n<<=1

print(get_index(8))

