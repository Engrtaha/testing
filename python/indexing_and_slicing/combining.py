import numpy as np
x = np.arange(1,17).reshape(4,4)

print("Original Array:")
print(x)
print("Slicing specific rows and columns:")
print(x[0:,[1,2]])
