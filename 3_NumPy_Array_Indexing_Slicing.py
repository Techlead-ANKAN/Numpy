# Array Indexing in NumPy - It is the same as indexing in python lists or tuple etc.

import numpy as np

a = np.array([1,2,3,4])
print(f"2nd element in 1d array = {a[1]}")



# [
#     [1,2,3,4]
#     [5,6,7,8]
#                 ]
b = np.array([[1,2,3,4], [5,6,7,8]])
print(f"2nd element in 2d array = {b[0, 1]}")



#  Slicing in NumPy Arrays

# Slicing in NumPy is similar to Python lists or tuples.
# [start:end:step]

a = np.array([1,2,3,4])
print(f"Slicing of array a = {a[1:3]}")
print(f"Slicing of array a = {a[1:3:2]}")

b = np.array([[1,2,3,4], [5,6,7,8]])
print(f"Slicing of array b = {b[0, 1:3]}")

