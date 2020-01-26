



s = {1,2,3,4,5}

s.add(11)
print(s)

# s.remove(30)
print(s)

s.discard(50)
print(s)


t = {1,2}


## subset checks
print(t==s)
print(s>t)

## remove elements not in s
print(s-t)