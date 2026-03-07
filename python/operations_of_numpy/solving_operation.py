import numpy as np
coefficients = np.array([[2,1],[-3,6]])
output = np.array([5,0])
solutions = np.linalg.solve(coefficients, output)
print("The solutions of the second degree equations are: ")
print(solutions)