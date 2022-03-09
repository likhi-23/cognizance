#Multiplying a matrix using numpy
import numpy as np
  
# creating two matrices
k = [[3, 2], [9, 3]]
l = [[8, 5], [6, 2]]
print("matrix k :")
print(k)
print("matrix l :")
print(l)
result = np.dot(k, l)
print("The Matrix multiplication is :")
print(result)
