'''
Problem 2. For each of the following items, write a function in Python 3.x that, given an
integer n, returns the sum of the first n terms of the series in the Leibniz formula.
e. Construct a Python dictionary and compute the sum of the terms in the dictionary.

Solution:
Using a loop for the calculation of every term and adding to a dictionary. Then, all of them sum.
N as input determines an integer.
'''

def LeibnizFormula (N):
    # N must be a positive number
    if N > 0 :
       Term_dictionary = {0:1}
       for i in range(1,N,1):
          
          # calculation of every term and adding to a dictionary
          Term_dictionary[i] = ((-1)**i / (2*i +1))
          
       return sum(Term_dictionary.values())   

    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")
        
# N=6              
# print(LeibnizFormula(N))
