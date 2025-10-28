import numpy as np

print("Enter Matrix A")
r=int(input("enter no of rows and colimns"))
c=int(input("enter no of colimns"))
a=np.zeros((r,c),dtype=int)



for i in range(r):
    for j in range(c):
        a[i][j]=int(input())


print("Enter Matrix B")
r=int(input("enter no of rows and colimns"))
c=int(input("enter no of colimns"))
b=np.zeros((r,c),dtype=int)



for i in range(r):
    for j in range(c):
        b[i][j]=int(input())
print(np.multiply(a,b))




