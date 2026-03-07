import pandas as pd
variable = pd.Series([4,6,7,8,3,2], index=['a','d','e','c','b','f'])
a = variable.sort_index()
b = variable.sort_values()
c = variable.isin([4,7])
d = variable[variable.isin([4,7])]
e = variable.values
f = list(variable.items())

print("none of the applied methods:")
print(variable)
print("after sorting by index:")
print(a)
print("after sorting by values:")
print(b)
print("after filtering(boolean mask):")
print(c)
print("after filtering:")
print(d)
print("after getting values:")
print(e)
print("after getting both index and values:")
print(f)
