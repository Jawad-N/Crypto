import math
from copy import deepcopy
# Using Optimal irreducible polynomials for Pentium-type 32-bit processor



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
    res = [0] * (p1.m + p2.m + 1)
    for i in range(len(p1.pol)):
        for j in range(len(p2.pol)):
            res[i+j] += p1.pol[i] * p2.pol[j] # can implemented in O(nlogn using FFT) 
    for i in range(len(res)):
        res[i] %= 2
    return polynomial(res)

class polynomial(object):

    def __init__(self, L): 
        self.m = len(L)-1
        self.pol = deepcopy(L)
        for i in range(len(L)):
            self.pol[i] %= 2
      

    def add(self, other):
        assert(self.m == other.m), "error"
        res = []

        for i in range(self.m+1):
            res.append( self.pol[i] + other.pol[i] )
            res[-1] %= 2
        return polynomial(res)
    

    def subtract(self,other):
        #We are subtracting the second polynomial from the first polynomial
        res = [0] * (self.m + 1)
        for i in range( min(other.m, self.m) ):
            if(self.pol[i] < other.pol[i]):
                res[i] = 1
            else:
                res[i] = self.pol[i] - other.pol[i]
        return polynomial(res)
    

    def division(self,other):
        current = polynomial( self.pol )
        ans = polynomial( [0] * (other.m + 1) )
        rem = polynomial( [0] * (other.m + 1) )
        while( current.degree() >= other.degree() ):
            ###Inf loop
            ans.pol[ current.degree() - other.degree() ] = 1
            temp = polynomial( [0] * ( current.degree()-other.degree()+1 ) )
            temp.pol[-1] = 1
            current = current.subtract( mul( other, temp ) ) # here we use the first multiplication that is not modular cause we need division to stay in the field

        rem = current
        return ans, rem
    



    def multiplication(self,other):
        curr = mul(self, other)
        return curr.division(D[self.m])[1] 
    # returning the remainder of the division between the polynomial of 
    # the regular multiplication ignoring the field limits, which is then
    # moduloed with the field irreducible polynomial


    def degree(self):
        for i in range(len(self.pol)-1,-1,-1):
            if(self.pol[i] == 1):
                return i
        return -1


 

    def modularInverse(self):

        mod = D[self.m]
        print("here: ",self.m)
        zero = [0] * ( self.m+1 )
        one = [0] * ( self.m+1 )
        one[0] = 1
        A = [polynomial(one), polynomial(zero), mod]
        B = [polynomial(zero), polynomial(one), self]
        print(mod)
        print("here")
        print(self)
        one = polynomial(one)
        while( not (B[2] == one) ):
            (Q, R) = A[2].division(B[2])
            print("Qutoient & remainder: ", Q, R)

            C = [0, 0, 0]
            C[0] = A[0].subtract( Q.multiplication(B[0]) )
            C[1] = A[1].subtract( Q.multiplication(B[1]) )
            C[2] = R
            for j in range(3): print(C[j].m)
            print('\n')
            A = B
            B = C

        return B[1]
    

    def __eq__(self, other):
        if( self.m != other.m ): return False
        else:
            for i in range( min( self.m, other.m ) ):
                if(self.pol[i] != other.pol[i] ): 
                    return False
            return True
       

    def __str__(self):
        cond = False
        ans = []
        for i in range(len(self.pol)-1,-1,-1):
            if(self.pol[i] != 0):
                cond = True
                ans.append(f"x^{i}")
        if(len(ans) == 0): return "0"
        else: return " + ".join(ans)


m3 = [0] * 4
m8 = [0] * 9
m113 = [0] * 114
m131 = [0] * 132
m163 = [0] * 164
m193 = [0] * 194
m233 = [0] * 234
m239 = [0] * 240
m283 = [0] * 284 
m409 = [0] * 410
m571 = [0] * 572
m3[0] = m3[1] = m3[3] = 1
m8[0] = m8[1] = m8[3] = m8[4] = m8[8] = 1
m113[0] = m113[15] = m113[113] = 1
m131[0] = m131[3] = m131[65] = m131[97] = m131[131] = 1
m163[0] = m163[3] = m163[97] = m163[99] = m163[163] = 1
m193[0] = m193[73] = m193[193] = 1
m233[0] = m233[9] = m233[105] = m233[201] = m233[233] = 1
m239[0] = m239[47] = m239[111] = m239[207] = m239[239] = 1
m283[0] = m283[27] = m283[219] = m283[249] = m283[283] = 1
m409[0] = m409[57] = m409[185] = m409[377] = m409[409] = 1
m571[0] = m571[417] = m571[475] = m571[507] = m571[571] = 1

m3 = polynomial(m3)
m8 = polynomial(m8)
m113 = polynomial(m113)
m131 = polynomial(m131)
m163 = polynomial(m163)
m193 = polynomial(m193)
m233 = polynomial(m233)
m239 = polynomial(m239)
m283 = polynomial(m283)
m409 = polynomial(m409)
m571 = polynomial(m571)

D = {
    3 : m3    ,
    8 : m8    ,
    113: m113 ,
    131: m131 ,
    163: m163 ,
    193: m193 , 
    233: m233 ,
    239: m239 ,
    283: m283 ,
    409: m409 ,
    571: m571

}


L = [ 1, 1, 1, 0, 1, 0, 1, 0, 0 ]
L2 = [ 1, 1, 0, 0, 0, 0, 0, 1, 0 ]

poly1 = polynomial(L)
poly2 = polynomial(L2)
print(poly2.modularInverse())

L3 = [1,0,1,0]
poly3 = polynomial(L3)  
print(poly3.modularInverse())






