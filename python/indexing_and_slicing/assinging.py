import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10])
x[0]=100
x[0:5]=10
x[5:]=20,30,40,50,60
print(x)