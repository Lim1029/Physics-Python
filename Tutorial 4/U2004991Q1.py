def f(x):
    return 3 - 2**x

def bisec(a,b):
    m = (a+b)/2
    f_m = f(m)
    while abs(f_m) >= 0.1:
        if f_m > 0:
            a = m
            m = (a+b)/2
            f_m = f(m)
        else:
            b = m
            m = (a+b)/2
            f_m = f(m)
    return m  
    
print("x =" ,bisec(0,2))
