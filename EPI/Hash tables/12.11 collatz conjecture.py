



def collatz_conjecture(no,oracle):

    # if no==1 or (no&~(no-1))^no==0:
    #     return True
    while no not in oracle:
        if no%2 == 1:
            oracle.add(no)
            no = 3*no + 1
        else:
            oracle.add(no)
            no = no/2
    return True

oracle = {1}
for i in range(100000):
    print(collatz_conjecture(i,oracle))

print(len(oracle))



