import numpy as np
array = np.array([1, 2, 3, 4, 5,6,7,8,9,10])
condition = array > 5

new_condition = (array!=8) & (array>=6)
print("it's original condition in integer values:")
print(array[condition])
    
print("it's new condition in integer values:")
print(array[new_condition])
print("it's boolean mask:")
print(array == 5)