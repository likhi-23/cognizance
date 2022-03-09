from numpy import *
a=array([])
b=int(input('First Number:'))
c=int(input('Last Number:'))
for p in range(b,c):
    a=append(a,p)
    for p in range(5):
        a=append(a,0)
a=append(a,c)
print(a)
