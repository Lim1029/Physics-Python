from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return x**3 - 2

def secant(x_1,x_0):
    return x_1 - f(x_1)/(f(x_1)-f(x_0))*(x_1-x_0)

fig, (ax1, ax2) = plt.subplots(1, 2)

x_0 = 0
x_1 = 1
diff = 1
step = 1
while diff >= 0.001:
    x_next = secant(x_1,x_0)
    if step == 3:
        ax1.plot(x_next,f(x_next), "ro")
    else:
        ax1.plot(x_next,f(x_next), "bo")
    diff = abs(x_next-x_1)
    x_0 = x_1
    x_1 = x_next
    step += 1

print("x =", x_1)

x_0 = 1
x_1 = 0
diff = 1
step = 1
while diff >= 0.001:
    x_next = secant(x_1,x_0)
    if step == 3:
        ax2.plot(x_next,f(x_next), "ro")
    else:
        ax2.plot(x_next,f(x_next), "bo")
    diff = abs(x_next-x_1)
    x_0 = x_1
    x_1 = x_next
    step += 1

print("x =", x_1)

x_real = np.linspace(-5,5,100)
y_real = []
for i in x_real:
    y_real.append(f(i))


# ax1.title("Secant method with x0 = 0, x1 = 1")
ax1.set_title("Secant method with x0 = 0, x1 = 1")
ax1.plot(x_real,y_real, color="blue")
ax1.plot(x_real,np.zeros(100), color="blue")

# ax1.title("Secant method with x0 = 1, x1 = 2")
ax2.set_title("Secant method with x0 = 1, x1 = 0")
ax2.plot(x_real,y_real, color="blue")
ax2.plot(x_real,np.zeros(100), color="blue")


plt.show() 
