import math
m = 163
class polynomial(object):
    def __init__(self, L):
        self.m = len(L)
        self.pol = L

    def add(self, other):
        assert(self.m == other.m), "error"

    def subtract(self,other):
        assert(self.m == other.m), "error"
        #We are subtracting the second polynomial from the first polynomial
        for i in range(self.m):
            if(self.pol[i] < other.pol[i]):
                self.pol[i] = 1
            else:
                self.pol[i] = self.pol[i] - other.pol[i]
        

    def multiplication(self,other):

    def inverse(self, other):
        
    