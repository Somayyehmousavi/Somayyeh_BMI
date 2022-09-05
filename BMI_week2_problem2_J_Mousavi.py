'''
Problem 2. For each of the following items, write a function in Python 3.x that, given an
integer n, returns the sum of the first n terms of the series in the Leibniz formula.

J. Combine the first and second terms, the third and fourth terms, etc. to change this
series from an alternating to a non-alternating series and compute the sum of the
combined terms.

Solution:
Using a loop for the calculation of every term and adding to an array. Then,Negative and
Positive terms are separated. After that, they are combined to make a new array and all
of them are sum.
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
       
       if len (Term_Positive) > len (Term_Negative): 
           Term_Negative =np.append(Term_Negative,0)
       
       newTerm_array = Term_Negative + Term_Positive
       print(newTerm_array)
       return (sum(newTerm_array))
   
    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")
        
#N = 6            
#print(LeibnizFormula(N))

