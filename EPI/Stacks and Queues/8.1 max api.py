

## o(n) space
class Stack:
    def __init__(self):
        self.stack = []
        self.max = float("-inf")

    def push(self,val):
        self.max = max(val,self.max)
        self.stack.append((val,self.max))

    def popp(self):
        self.stack.pop()

    def get_max(self):
        if len(self.stack)>0:
            return self.stack[-1][1]


## worst case o(n) but one average less space solution..
class Stack_Improved:
    def __init__(self):
        self.stack = []
        self.max_stack = []
        # self.max = float("-inf")

    def push(self, val):
        if len(self.stack)>0:
            if val==self.max_stack[-1][0]:
                self.max_stack[-1][1] += 1
            elif val>self.max_stack[-1][0]:
                self.max_stack.append((val,1))
        else:
            self.max_stack.append((val,1))
        self.stack.append(val)
        # self.max = max(val, self.max)
        # self.stack.append((val, self.max))

    def popp(self):
        elem = self.stack.pop()
        if elem == self.max_stack[-1][0]:
            if self.max_stack[-1][1]>1:
                self.max_stack[-1][1] -= 1
            else:
                self.max_stack.pop()

    def get_max(self):
        if len(self.stack) > 0:
            return self.max_stack[-1][0]



s = Stack_Improved()

s.push(1)
print(s.stack)
print(s.get_max())

s.push(-11)
print(s.stack)
print(s.get_max())

s.push(3)
print(s.stack)
print(s.get_max())

s.popp()
print(s.stack)
print(s.get_max())

