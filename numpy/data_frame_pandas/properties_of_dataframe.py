import numpy as np  
import pandas as pd
a = np.random.randint(10,50,size=6)
b= np.random.randint(10,50,size=6)
c = np.random.randint(10,50,size=6)
d = np.random.randint(10,50,size=6)
dict_example = {"col1": a, "col2": b, "col3": c, "col4": d}
df = pd.DataFrame(dict_example)
x = df.describe()
y = df.info()
z = df.head()
t = df.tail()
n = df.columns
m = df.columns = ["new1","new2","new3","new4"]
p = df.values



print("Summary statistics of the DataFrame:")
print(x)
print("Info about the DataFrame:")
print(y)
print("First few rows of the DataFrame:")
print(z)
print("Last few rows of the DataFrame:")
print(t)
print("Column names of the DataFrame:") 
print(n)
print("New column names:")
print(m)
print("Values of the DataFrame:")
print(p)