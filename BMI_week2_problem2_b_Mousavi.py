'''
Problem 2.
For each of the following items, write a function in Python 3.x that, given an
integer n, returns the sum of the first n terms of the series in the Leibniz formula.

Use a for-loop with the quantity (-1)**n to determine whether to add or subtract
each term.

Solution:
Using a loop for the calculation of every term and using the the quantity (-1)**n to add or subtract.
N as input determines an integer.
'''
def LeibnizFormula (N):
    # N must be a positive number
    if N > 0 :
       sum= 0
       for i in range(0,N,1):
           
          # determination to add or subscribe
          term = 1 / (2*i +1) 
          if (-1)**i > 0:
              sum+= term
             
          else: 
              sum-= term 
        
       return sum
    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")
        
# N =  110000        
# print(LeibnizFormula(N))