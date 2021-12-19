a = []
for i in range(n_node-1):
    a.append((y_array[i+1]-y_array[i])/(x_array[i+1]-x_array[i]))

b = []
for i in range(n_node-2):
    b.append((a[i+1]-a[i])/x_array[i+2]-x_array[i])

c = []
for i in range(n_node-3):
    c.append((b[i+1]-b[i])/x_array[i+3]-x_array[i])

print(a[0])
print(b[0])
print(c[0])