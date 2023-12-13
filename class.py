import math
from copy import deepcopy
import tkinter as tk
from tkinter import ttk

# Using Optimal irreducible polynomials for Pentium-type 32-bit processor - List in the sent article


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
    
    def __mul(p1,p2):
        assert( type(p1) == polynomial and type(p2) == polynomial ), "multiplying non polinomial objects"
        res = [0] * (p1.m + p2.m + 1)
        for i in range(len(p1.pol)):
            for j in range(len(p2.pol)):
                res[i+j] += p1.pol[i] * p2.pol[j] # can implemented in O(nlogn using FFT) 
        for i in range(len(res)):
            res[i] %= 2
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
            current = current.subtract( other.__mul( temp ) ) # here we use the first multiplication that is not modular cause we need division to stay in the field
        rem = current
        return ans, rem
    
    def multiplication(self,other):
        curr = self.__mul( other )
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
            C = [0, 0, 0]
            C[0] = A[0].subtract( Q.multiplication(B[0]) )
            C[1] = A[1].subtract( Q.multiplication(B[1]) )
            C[2] = R
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

root = tk.Tk()

root.title("Polynomial Operator")


label = tk.Label(root, text="First Polynomial: ", font=("Arial", 12))
label.pack()
poly_input = tk.StringVar()
poly_input = tk.Entry(root, textvariable=poly_input, width=70)
poly_input.pack()


label2 = tk.Label(root, text="Second Polynomial: ", font=("Arial", 12))
label2.pack()
poly_input2 = tk.StringVar()
poly_input2 = tk.Entry(root, textvariable=poly_input2, width=70)
poly_input2.pack()

selected_operation = tk.StringVar()
selected_operation.set("Select operation")
operation = ttk.Combobox(root, textvariable=selected_operation, width=50)
operation['values'] = ('Addition', 'Subtraction', 'Multiplication', 'Division', 'Modular Inverse')
operation.pack()

def perform_operation():
    poly = poly_input.get()
    poly2 = poly_input2.get()
    poly = polynomial([int(x) for x in poly.split()])
    poly2 = polynomial([int(x) for x in poly2.split()])
    operation = selected_operation.get() 

    print(poly)
    print(poly2)

    if operation == 'Addition':
        result = poly.add(poly2)
    elif operation == 'Subtraction':
        result = poly.subtract(poly2)
    elif operation == 'Multiplication':
        result = poly.multiplication(poly2)
    elif operation == 'Division':
        result = poly.division(poly2)
    elif operation == 'Modular Inverse':
        result = poly.modularInverse()
    else:
        result = 'Error'
    # Display the result in the output field
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

operation_button = tk.Button(root, text="Perform Operation", command=perform_operation)
operation_button.pack()


result_text = tk.Text(root, height=2, width=50)
result_text.pack()


root.mainloop()



