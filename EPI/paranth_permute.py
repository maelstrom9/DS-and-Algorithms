


# op = {"(":1,}

###TURNED OUT TO BE GOOD TEMPLATE FOR PERMUTATIONS PROBLEMS>.. ###

def form_possible_perm(res,n,formed):
    if n==0 and formed==0:
        return [res]

    temp = []

    if formed<3 and n!=0:
        temp.extend(form_possible_perm(res+"(",n-1,formed+1))
    if formed>0:
        temp.extend(form_possible_perm(res+")",n,formed-1))

    return temp


print(form_possible_perm("",3,0))

print(hash("a"))
