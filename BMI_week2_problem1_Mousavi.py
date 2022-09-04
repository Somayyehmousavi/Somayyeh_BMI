'''
Problem 1.
Write a function in Python 3.x that, given an integer n, returns the sum of
the first n terms of the series in the Leibniz formula.

Solution:
Using a loop for the calculation of every term and adding it to the sum of other 
previous terms. 
N as input determines  an integer.

'''
def LeibnizFormula (N):
    # N must be a positive number
    if N > 0 :
       sum= 0
       for i in range(0,N,1):
           
          sum += (-1)**i / (2*i +1)
        
       return sum
   
    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")
        
        
#N=10000   
#print(LeibnizFormula(N))