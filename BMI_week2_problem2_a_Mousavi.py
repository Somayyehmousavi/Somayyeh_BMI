'''
Problem 2.
For each of the following items, write a function in Python 3.x that, given an
integer n, returns the sum of the first n terms of the series in the Leibniz formula.

a. Use a for-loop and an if-statement with the modulo operator % to determine whether
to add or subtract each term.

Solution:
Using a loop for the calculation of every term and Using the operator %  to add or subtract.
N as input determines an integer.

'''
def LeibnizFormula (N):
    # N must be a positive number
    if N > 0 :
       sum= 0
       for i in range (0,N,1):
           
          # determination to add or subscribe
          if ((-1)**i % (2*i +1))>= 0 :
              
              sum+= (-1)**i / (2*i +1) 
             
          else:    
              sum-= (-1)**i / (2*i +1)
        
       return sum
    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")
        
# N=10000       
# print(LeibnizFormula(N))
