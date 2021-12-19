from typing import Match
from matplotlib import pyplot as plt


import numpy as np

def f(x):
    return x**2 - 4*np.sin(x)

def f_prime(x):
    return 2*x - 4*np.cos(x)

def newton_rapson(x):
    return x-f(x)/f_prime(x)



x = 3
plt.plot(x,f(x), "bo", color="green")
diff = 1
while diff >= 0.001:
    x_next = newton_rapson(x)
    plt.plot(x_next,f(x_next), "bo", color="green")
    diff = abs(x_next-x)
    x = x_next

print("x =", x)

x_real = np.linspace(-5,5,100)
y_real = []
for i in x_real:
    y_real.append(f(i))

plt.title("Newton Rapson Method")
plt.plot(x,f(x), "bo", color="green")
plt.plot(x_real,y_real, color="blue")
plt.plot(x_real,np.zeros(100), color="blue")
plt.show() 
