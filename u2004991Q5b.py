#question 5b

import math as mt
#import the library used to construct table
from prettytable import PrettyTable

#the same code from question 3 equation 1
def e_exp_x(order,x):
    sum = 0
    for n in range (order+1):
        # (((-1)**n)*(x**n))/mt.factorial(n) is the general formula for n_th term
        sum += (((-1)**n)*(x**n))/mt.factorial(n)
    return sum

myTable = PrettyTable(['order','result','error'])

#set the value of x and get the true value of the expression
x = 1
true_val = mt.e**(-x)

#try and tabulate result with increment value of order starting from zero order
for order in range(10):
    result = e_exp_x(order=order,x=x)
    error = abs(true_val-result)
    myTable.add_row([order,result,error])

print("value of x: ",x)
print("true value: ",true_val)
print(myTable)

#conclusion: with x set to 0.1, expansion up to one order gives error within 10^-3
#conclusion: with x set to 0.1, expansion up to 3 order gives error within 10^-6