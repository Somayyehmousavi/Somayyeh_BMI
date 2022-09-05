'''
Problem 2. For each of the following items, write a function in Python 3.x that, given an
integer n, returns the sum of the first n terms of the series in the Leibniz formula.
d. Construct a Python set and compute the sum of the terms in the set.

Solution:
Using a loop for the calculation of every term and adding to a set. Then, all of them sum.
N as input determines an integer.
'''

def LeibnizFormula (N):
    # N must be a positive number
    if N > 0 :
       Term_set = set()
       for i in range(0,N,1):
           
          # calculation of every term and adding to a set
          Term_set.add ((-1)**i / (2*i +1))
        
       return sum (Term_set)
    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")

N = 6              
print(LeibnizFormula(N))
