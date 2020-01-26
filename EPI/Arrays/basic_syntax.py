import copy
import bisect

b =[1,2,2,3]
b.remove(2)
print(b)

## copy

a = b
b.append(4)
print(a)

c = list(a)
a.append(5)
print(c,b)

a = [1,2,3,[4,2],5]
d = copy.copy(a)
d[3][0]=1
d[4] = 2
print(a,d)


## bisect
arr = [1,2,4,6,10]
## returns position where the no has to be
## inserted to keep the list sorted ## default right
print(bisect.bisect(arr,7))
print(bisect.bisect_right(arr,7))
print(bisect.bisect_left(arr,6))

## reversed iterator..
print([i for i in reversed(arr)])

##A[i:j:k] ?  its like how range works..

## product list comprehensions...
A = [1,2,3]
B = ['a','b']
res = [(x,y) for x in A for y in B]
print(res)

##2d to 1d
Z = [['a','b'],['c','d']]
res = [i for row in Z for i in row]
print(res)

##two levels of looping
A = [[1,2],[3,4]]
res = [[x+1 for x in row] for row in A]
print(res)