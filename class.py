import math
class polynomial(object):
    def __init__(self, L):
        self.m = len(L)
        self.pol = L

    def add(self, other):
        assert(self.m == other.m), "error"
        assert(self.m == other.m), "error"
        res = []
        print(len(self.pol))
        print(len(other.pol))
        for i in range(self.m):
            res.append( self.pol[i] + other.pol[i] )
            res[-1] %= 2
        return polynomial(res)
            


    def subtract(self,other):
        assert(self.m == other.m), "error"
        #We are subtracting the second polynomial from the first polynomial
        for i in range(self.m):
            if(self.pol[i] < other.pol[i]):
                self.pol[i] = 1
            else:
                self.pol[i] = self.pol[i] - other.pol[i]


    def multiplication(self,other):
        assert(self.m == other.m), "error"

    def inverse(self, other):
        assert(self.m == other.m), "error"

    def __str__(self):
        cond = False
        ans = []
        for i in range(self.m-1,-1,-1):
            if(self.pol[i] == 1):
                cond = True
                ans.append(f"x^{i}")
        if(len(ans) == 0): return "0"
        else: return " + ".join(ans)


L = [1,2,3,4,5,6]
L2 = [0,0,0,0,1,1]
poly1 = polynomial(L)
poly2 = polynomial(L2)
print(poly1.add(poly2))


    