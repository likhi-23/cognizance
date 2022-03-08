import numpy as np
given_vector = np.array([10, 11, 12, 13, 14])
print("Original array  ")
print(given_vector)
a = 5
new_vector = np.zeros(len(given_vector) + (len(given_vector)-1)*(a))
new_vector[::a+1] = given_vector
print("\n New array ")
print(new_vector)
