'''
NumPy Arrays - The arrays object in NumPy is known as ndarray. We can create ndarray object using array() function.

ndarray - To create an ndarray we can pass list, tuple or any array like objects into the array() method,  which will convert it into an ndarray. 
'''

import numpy as np

# Passing List
myarrl = np.array([1,2,3,4]) # creating ndarray
print(myarrl)
print(type(myarrl))  # type of myarrl

# Passing Tuple
myarrt = np.array((1,2,3,4)) # creating ndarray
print(myarrt)
print(type(myarrt))  # type of myarrt


# Dimension in Arrays

# 1. 0-D Array (Scalar)
arr_0d = np.array(12)
print(arr_0d)


# 2. 1-D Array
arr_1d = np.array([10, 20, 30, 40])
print(arr_1d)


# 3. 2-D Array
arr_2d = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(arr_2d)


# 4. 3-D Array
arr_3d = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print(arr_3d)




# Checking number of Dimension of a NumPy Array

# ndim - It is a numpy attribute that returns an integer which tells us how many dimensions does the array have.

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(f"Dimension of array 'a' = {a.ndim}")
print(f"Dimension of array 'b' = {b.ndim}")
print(f"Dimension of array 'c' = {c.ndim}")
print(f"Dimension of array 'd' = {d.ndim}")



# Higher Dimensional Arrays using "ndmin"

e = np.array([1,2,3,4], ndmin=3)
print(e)
print(f"No.of dimensions in array 'e' = {e.ndim}")