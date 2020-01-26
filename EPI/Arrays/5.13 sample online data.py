import random

class SampleOnline:
    def __init__(self,k):
        self.k = k
        self.result = []
        self.n = 0

    def sample(self,elem):
        self.n+=1
        ## probability of selecting n+1 th packet
        prob = min(1,self.k/self.n)

        sel_prob = random.uniform(0,1)
        if len(self.result)<2:
            self.result.append(elem)
            return
        if sel_prob<=prob:
            ##remove random element
            rem_index = random.randint(0,self.k-1)
            self.result[rem_index] = elem

c = SampleOnline(2)

c.sample(1)
print(c.result)
c.sample(2)
print(c.result)
c.sample(3)
print(c.result)
c.sample(4)
print(c.result)
c.sample(5)
print(c.result)
c.sample(6)
print(c.result)
c.sample(10)
print(c.result)
c.sample(11)
print(c.result)
c.sample(12)
print(c.result)
c.sample(13)
print(c.result)
c.sample(14)
print(c.result)
c.sample(15)
print(c.result)



