'''
Problem 2. For each of the following items, write a function in Python 3.x that, given an
integer n, returns the sum of the first n terms of the series in the Leibniz formula.
f. Construct a NumPy array and compute the sum of the terms in the array

Solution:
Using a loop for the calculation of every term and adding to a array. Then, all of them sum.
N as input determines an integer.
'''

import numpy as np
def LeibnizFormula (N):
    # N must be a positive number
    if N > 0 :
        
       Term_array = np.zeros (N)
       for i in range(0,N,1):
          
          Term_array[i] = ((-1)**i / (2*i +1))
          
       return sum(Term_array[:]) 
   
    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")
        
N=5              
print(LeibnizFormula(N))

