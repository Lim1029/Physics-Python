import numpy as np
import matplotlib.pyplot as plt

# define function square root of x
def fun(x):
   return np.sqrt(x)

#define interval, start and end point and number of node
interval = [0,1]
start = interval[0]
end = interval[1]
n_node = 16

#create x and y with equally spaced nodes (linspace)
x_array = np.linspace(start,end,n_node)
y_array = fun(x_array)

#Specific Case (only for n_nodes = 4), i did this to find the pattern so that i could make a general case

a = []
for i in range(n_node-1):
    a.append((y_array[i+1]-y_array[i])/(x_array[i+1]-x_array[i]))

b = []
for i in range(n_node-2):
    b.append((a[i+1]-a[i])/(x_array[i+2]-x_array[i]))

c = []
for i in range(n_node-3):
    c.append((b[i+1]-b[i])/(x_array[i+3]-x_array[i]))

coefff = [a[0],b[0],c[0]]

# General case, for any n_nodes
coefff = []
g = y_array.copy()
for k in range(1,n_node):
    a = []
    for i in range(n_node-k):
        a.append((g[i+1]-g[i])/(x_array[i+k]-x_array[i]))
    coefff.append(a[0])
    g = a.copy()

# calculate y_pred using the interpolation formula: a0 + a1(x-x0)...
y_pred = []
for x in x_array:
    y = y_array[0]
    for i in range(n_node-1):
        y_i = coefff[i]
        for j in range(i+1):
            y_i *= (x-x_array[j])
        y += y_i
    y_pred.append(y)

#plot the absolute different between prediction y and real y, versus x
plt.plot(x_array,abs(y_array-y_pred), 'bo')
plt.show()

#plot interpolation equation and real equation in a graph
# plt.plot(x_array,y_pred, "bo", color="green")
# plt.plot(x_array,y_array, "bo", color="red")