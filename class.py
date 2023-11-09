import math

#def irreducible(m): # given GF(2^m) we want to return the irreducible polynomial of this field
                    # we can't do it by bruteforce, for big m it is computationally impossible

#we always consider the irreducible polynomial that is m(x) = x^m + x + 1
#we know it is irreducible because m(0) = 1 and m(1) = 1 thus it has no roots --> it cannot be factorized
 
def leftShift(L):# careful also affects L, this multiplies the polynomial by x
    n = len(L)
    L.append(0)
    for i in range(n, 0, -1):
        L[i] = L[i-1]
    L[0] = 0
    return L

def rightShift(L):# this divides the polynomial by x, if 1 exists in the polynomial, then it substract it before doing so
    n = len(L)
    for i in range(1,n):
        L[i-1] = L[i]
    L.pop()
    return L

def mul(p1,p2):
    assert( type(p1) == polynomial and type(p2) == polynomial ), "multiplying non polinomial objects"
    res = [0] * (p1.m + p2.m - 1)
    for i in range(p1.m):
        for j in range(p2.m):
            res[i+j] += p1.pol[i] * p2.pol[j]
    for i in range(len(res)):
        res[i] %= 2
    return polynomial(res)

class polynomial(object):
    def __init__(self, L):
        self.m = len(L)
        self.pol = L
        for i in range(len(L)):
            self.pol[i] %= 2
        for i in range(self.m):
            self.pol[i] %= 2

    def modulo(self):
        # check the field over which the polynomial is created in self.m
        # and apply modulo m(x) which is x^m + x + 1
        
        len(self.pol)



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
        #We are subtracting the second polynomial from the first polynomial
        res = [0]*self.m
        for i in range(self.m):
            if(self.pol[i] < other.pol[i]):
                res[i] = 1
            else:
                res[i] = self.pol[i] - other.pol[i]
        return polynomial(res)
        

    


    def multiplication(self,other):
        assert(self.m == other.m), "error"

    def degree(self):
        for i in range(self.m-1,-1,-1):
            if(self.pol[i] == 1):
                return i

    def division(self,other):
        current = polynomial(self.pol)
        ans = polynomial([0]*len(self.pol))
        rem = polynomial([0]*other.m)
        while(current.degree() >= other.degree()):
            ans.pol[current.degree() - other.degree()] = 1
            temp = polynomial([0]*(current.degree()-other.degree()+1))
            temp.pol[-1] = 1
            current = current.subtract(mul(other,temp))
            print(current)
        rem = current
        return ans, rem

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


L = [1,0,0,1,1,1,1,0,1,1,0,1,0,1]
L2 =[1,1,0,1,1,0,0,0,1,0,0,0,0,0]
poly1 = polynomial(L)
poly2 = polynomial(L2)
print(poly1)
print(poly2)
print('\n')
poly3 = poly1.division(poly2)



    