#question 4

import numpy as np
from prettytable import PrettyTable

#a function based on the formula given, taking x as input
def f_x(x):
    return ((np.e**x)-1)/x

#create a table with PrettyTable library, create 3 columns: value of i, value of x, value of the calculation result
myTable = PrettyTable(['i','x','result','r_error'])

#initiate the value i as 0
i = 0
#give ans a arbitraty value
ans = 1
#set approximate value as 1 and previous approximate as 0
app_val = 1
prev_appr = 0

#repeat the calculation as long as the ans is not zero
while (ans != 0):
    x = 2**(-i)
    ans = f_x(x)
    #calculate the relative error based on the formula: |current approximation-previous approximation|/approximation value
    r_error = abs(ans-prev_appr)/app_val
    #add a row with related info to the table
    myTable.add_row([i,x,ans,r_error])
    #increment the value of i by 1
    i += 1
    #update previous approximation with current approximation value
    prev_appr = ans

# print out the table and last i value)
print(myTable)
print("value of i that give the function zero: ", i-1)