from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return x*np.sin(x) - 1
def f_prime(x):
    return x*np.cos(x) + np.sin(x)

def newton_rapson(x):
    return x-f(x)/f_prime(x)

def f_secant(x_1,x_0):
    return x_1 - f(x_1)/(f(x_1)-f(x_0))*(x_1-x_0)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

def bisec(a,b):
    m = (a+b)/2
    ax1.plot(m,f(m), "ro")
    f_m = f(m)
    while abs(f_m) >= 0.000001:
        if f_m > 0:
            a = m
            m = (a+b)/2
            f_m = f(m)
        else:
            b = m
            m = (a+b)/2
            f_m = f(m)

        ax1.plot(m,f(m), "go")
    return m 

def newton(x):
    ax2.plot(x,f(x), "ro")
    diff = 1
    while diff >= 0.000001:
        x_next = newton_rapson(x)
        ax2.plot(x_next,f(x_next), "go")
        diff = abs(x_next-x)
        x = x_next
    return x_next

def secant(x_0,x_1):
    diff = 1
    ax3.plot(x_1,f(x_1), "ro")
    while diff >= 0.000001:
        x_next = f_secant(x_1,x_0)
        ax3.plot(x_next,f(x_next), "go")
        diff = abs(x_next-x_1)
        x_0 = x_1
        x_1 = x_next
    return x_1


x_0 = 0
x_1 = np.pi/2
print("Bisect Method, x =", bisec(x_1,x_0))
print("Newton Method, x =", newton(x_1))
print("Secant Method, x =", secant(x_0,x_1))


x_real = np.linspace(-5,5,100)
y_real = []
for i in x_real:
    y_real.append(f(i))

ax1.set_title("Bisect Method")
ax1.plot(x_real,y_real, color="b")
ax1.plot(x_real,np.zeros(100), color="b")

ax2.set_title("Newton Method")
ax2.plot(x_real,y_real, color="b")
ax2.plot(x_real,np.zeros(100), color="b")

ax3.set_title("Secant Method")
ax3.plot(x_real,y_real, color="b")
ax3.plot(x_real,np.zeros(100), color="b")

plt.show()