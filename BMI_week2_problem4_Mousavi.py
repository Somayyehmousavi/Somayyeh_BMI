# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 01:34:23 2022

@author: bcz
"""

import numpy as np
import matplotlib.pyplot as plt
import math
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
        
N=500
Y= np.pi*np.ones(N)
Yh = np.zeros(N)
for i in range(1,N+1,1):Yh[i-1] = LeibnizFormula(i)*4
error=abs(Y-Yh)

plt.figure(figsize=(3, 3))
plt.ylim(0,1);
plt.plot(error,'o')
plt.title('Absolute Error in the Calculating Pi Based on the Number of Terms in Leibniz Formula')
plt.xlabel('Numbers of Terms')
plt.ylabel('Absolute Error')