import numpy as np
f=int(input("First Number: "))
a=int(input("last number : "))
l=[]
for i in range(f,a+1):
    l.append(float(i))
a = np.array(l)
nz = 5
Z0 = np.zeros(len(a) + (len(a)-1)*(nz))
Z0[::nz+1] = a
print(Z0)
