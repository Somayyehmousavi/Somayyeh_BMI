def LeibnizFormula_problem1 (N):
    # N must be a positive number
    if N > 0 :
       sum= 0
       for i in range(0,N,1):
           
          sum += (-1)**i / (2*i +1)
        
       return sum

    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")
 
def LeibnizFormula_problem2a (N):
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
        
def LeibnizFormula_problem2b (N):
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
        
def LeibnizFormula_problem2c (N):
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

def LeibnizFormula_problem2d (N):
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
        
def LeibnizFormula_problem2e (N):
    # N must be a positive number
    if N > 0 :
       Term_dictionary = {0:1}
       for i in range(0,N,1):
          
          # calculation of every term and adding to a dictionary
          Term_dictionary[i] = ((-1)**i / (2*i +1))
          
       return sum(Term_dictionary.values())   

    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")

import numpy as np
def LeibnizFormula_problem2f (N):
    # N must be a positive number
    if N > 0 :
        
       Term_array = np.zeros (N)
       for i in range(0,N,1):
          
          Term_array[i] = ((-1)**i / (2*i +1))
          
       return sum(Term_array[:]) 
   
    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")
        

def LeibnizFormula_problem2g (N):
    # N must be a positive number
    if N > 0 :
       Term_array = np.zeros (N)

       for i in range(0,N,1):
          
          Term_array[i] = ((-1)**i / (2*i +1))

       Term_Negative = Term_array[1::2]
       Term_Positive = Term_array[::2]
       
       #print ("Term_Positive=", Term_Positive) , print ("Term_Negative=", Term_Negative)
       return (sum (Term_Positive) + sum (Term_Negative))
   
    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")
        

def LeibnizFormula_problem2j (N):
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
       #print(newTerm_array)
       return (sum(newTerm_array))
   
    # If N be a negative number 
    else:
        print("IT CAN NOT BE CALCULATED")
        
################################
import sklearn.metrics as met
N=10000
Y= np.pi*np.ones(N)
################################
Yh = np.zeros (N)
for i in range(1,N,1):Yh[i-1] = LeibnizFormula_problem1(i)*4
rmse = met.mean_squared_error(Y, Yh)**0.5
print('rmse_LeibnizFormula_problem1=',rmse)  
################################
Yh = np.zeros (N)
for i in range(1,N,1):Yh[i-1] = LeibnizFormula_problem2a(i)*4
rmse = met.mean_squared_error(Y, Yh)**0.5
print('rmse_LeibnizFormula_problem2a=',rmse) 
##############################
Yh = np.zeros (N)
for i in range(1,N,1):Yh[i-1] = LeibnizFormula_problem2b(i)*4
rmse = met.mean_squared_error(Y, Yh)**0.5
print('rmse_LeibnizFormula_problem2b=',rmse)
################################
Yh = np.zeros (N)
for i in range(1,N,1):Yh[i-1] = LeibnizFormula_problem2c(i)*4
rmse = met.mean_squared_error(Y, Yh)**0.5
print('rmse_LeibnizFormula_problem2c=',rmse)
##################################
Yh = np.zeros (N)
for i in range(1,N,1):Yh[i-1] = LeibnizFormula_problem2d(i)*4
rmse = met.mean_squared_error(Y, Yh)**0.5
print('rmse_LeibnizFormula_problem2d=',rmse)
####################################
Yh = np.zeros (N)
for i in range(1,N,1):Yh[i-1] = LeibnizFormula_problem2e(i)*4
rmse = met.mean_squared_error(Y, Yh)**0.5
print('rmse_LeibnizFormula_problem2e=',rmse)
######################################
Yh = np.zeros (N)
for i in range(1,N,1):Yh[i-1] = LeibnizFormula_problem2f(i)*4
rmse = met.mean_squared_error(Y, Yh)**0.5
print('rmse_LeibnizFormula_problem2f=',rmse)
######################################
Yh = np.zeros (N)
for i in range(1,N,1):Yh[i-1] = LeibnizFormula_problem2g(i)*4
rmse = met.mean_squared_error(Y, Yh)**0.5
print('rmse_LeibnizFormula_problem2g=',rmse)
#######################################
Yh = np.zeros (N)
for i in range(1,N,1):Yh[i-1] = LeibnizFormula_problem2j(i)*4
rmse = met.mean_squared_error(Y, Yh)**0.5
print('rmse_LeibnizFormula_problem2j=',rmse)

























