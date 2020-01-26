


def test_palindromicity(s):
    i = 0
    j = len(s)-1

    # c = 0  ## i<j property can be used instead
    while i<j:
        while not s[i].isalnum():
            i+=1
            # c+=1
        while not s[j].isalnum():
            j-=1
            # c+=1
        if s[i].lower()!=s[j].lower():
            return False
        else:
            i+=1
            j-=1
            # c+=2
    return True

print(test_palindromicity(",,,,,....amAna,nama"))