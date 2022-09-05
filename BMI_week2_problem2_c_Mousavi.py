'''
Problem 2. For each of the following items, write a function in Python 3.x that, given an
integer n, returns the sum of the first n terms of the series in the Leibniz formula.
c. Construct a Python list and compute the sum of the terms in the list.

Solution:
Using a loop for the calculation of every term and adding to a list. Then, all of them sum.
N as input determines an integer.
'''

def LeibnizFormula (N):
    # N must be a positive number
    if N > 0 :
       Term_list = []
       for i in range(0,N,1):
           
          # calculation of every term and adding to a list
          Term_list.append ((-1)**i / (2*i +1))
        
       return sum (Term_list)
    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")
 
N = 10000             
print(LeibnizFormula(N))
