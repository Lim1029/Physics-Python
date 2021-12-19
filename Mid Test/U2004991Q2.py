import numpy as np
import matplotlib.pyplot as plt

x_array = [-0.5,0,0.5]

def f(x):
    return 1/(x+1)

def lagrange(x):
    return x**2 - 3/2*x +1


y_pred_array = []
for i in x_array:
    y_pred_array.append(lagrange(i))

x_real = np.linspace(-0.5,0.5,100)
y_real = []
for i in x_real:
    y_real.append(f(i))

plt.title("Lagrange Polynomial Estimation")
plt.plot(x_array,y_pred_array, "bo", color="green")
plt.plot(x_real,y_real, color="blue")
plt.show() 