import numpy as np
x = np.zeros((10,10),dtype="int")
row = x.shape[0]
z = x.size
for i in range(row):
    x[i] = i
example = np.arange(1,17).reshape(4,4)    
list1 = [[0,3],[1,2]]
a = example[list1]
print(x)
print(row)
print(a)

print(z)