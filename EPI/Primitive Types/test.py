import sys,math,random
# print(sys.float_info)

## convert to binary string format
print(bin(14))
print(bin(13))

print(max(2,3))
print(max([1,-1,2,5]))

print(abs(-2.3))

## ceil and floor
print(math.ceil(2.17)) ## ceil--> higher int.
print(math.floor(3.14))## floor-->lower int.
# print(math.sqrt(9))

print(max(float("inf"),10))
print(min(float("-inf"),10))

## compare values
print(math.isclose(10,20,abs_tol=10))

##random
print(random.randrange(23))