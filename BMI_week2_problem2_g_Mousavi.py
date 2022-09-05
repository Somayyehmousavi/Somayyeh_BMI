'''
Problem 2. For each of the following items, write a function in Python 3.x that, given an
integer n, returns the sum of the first n terms of the series in the Leibniz formula.

g. Construct a NumPy array, use array indexing to compute the sum of the positive terms
in the array, use array indexing to compute the sum of the negative terms in the array,
and add the two sums together. You can write x[::2] to access the first, third, etc.
terms and x[1::2] to access the second, fourth, etc. terms.

Solution:
Using a loop for the calculation of every term and adding to an array. Then,Negative and
Positive terms are separated and both of them are sum.
N as input determines an integer.
'''

import numpy as np
def LeibnizFormula (N):
    # N must be a positive number
    if N > 0 :
       Term_array = np.zeros (N)

       for i in range(0,N,1):
          
          Term_array[i] = ((-1)**i / (2*i +1))

       Term_Negative = Term_array[1::2]
       Term_Positive = Term_array[::2]
       
       print ("Term_Positive=", Term_Positive) , print ("Term_Negative=", Term_Negative)
       return (sum (Term_Positive) + sum (Term_Negative))
   
    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")

N = 7              
print(LeibnizFormula(N))

