
import numpy as np


a=[1,2,3,4]
b=[2,3,4,5]

print(np.intersect1d(a,b))

print(np.union1d(a,b))
a=set(a)
b=set(b)
print(a|b)
print(a&b)
