#Program to find the solution for the given linear equations.
#Developed by: ROHITH S
#RegisterNumber:25008317
import numpy as np
a=np.array([[1,-3],[3,1]])
b=np.array([0,10])
print(np.linalg.solve(a,b))