

def spread_sheet_encoding(str_a):
    res = 0
    for c in str_a:
        res *= 26
        res += ord(c)-ord("A")+1
    return res



def spread_sheet_decoding(no):
    s = []
    while no:
        no, rem = divmod(no-1,26)
        s.append(chr(ord("A")+rem))
    return "".join(reversed(s))

print(spread_sheet_decoding(676))



print(spread_sheet_encoding("A"))

print(spread_sheet_encoding("ZZ"))

print(spread_sheet_encoding("AB"))

print(spread_sheet_encoding("AA"))

print(spread_sheet_encoding("ZZZ"))