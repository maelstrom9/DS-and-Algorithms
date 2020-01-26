
from heapq import heappushpop,heappush,heappop

class RunningMedian:

    def __init__(self):
        self.L = []   ## max_heap
        self.R = []   ## min_heap
        self.median = None


    def add(self,e):
        if not self.median:
            self.median = e
            heappush(self.L,-e)
        else:
            ## always put in mn heap first and get the smallest send to max heap
            heappush(self.R,-heappushpop(self.L,-e))
            ## In case sizes differ, adjust
            if len(self.R)>len(self.L):
                heappush(self.L,-heappop(self.R))
            if len(self.L) == len(self.R):
                self.median = (abs(self.L[0])+self.R[0])/2.0
            else:
                self.median =  abs(self.L[0])




rm = RunningMedian()

for i in [1,0,3,5,2,0,1]:
    rm.add(i)
    print(rm.median)