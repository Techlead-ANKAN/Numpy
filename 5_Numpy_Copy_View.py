import numpy as np


'''
Copy in NumPy

Definition: A copy is a completely independent object. Changes made in the copy do not affect the original array and vice versa.

Memory: A new memory location is allocated for the copied array.

Use Case: Use a copy when you need to modify an array without affecting its original data
'''


# Original array
arr = np.array([1, 2, 3, 4])

# Create a copy
arr_copy = arr.copy()

# Modify the copy
arr_copy[0] = 10

print("Original array:", arr)  # [1 2 3 4]
print("Copy array:", arr_copy)  # [10 2 3 4]



'''
View in Numpy

Definition: A view is a new array object that shares the same data as the original array. Changes made to the view affect the original array and vice versa.

Memory: No new memory is allocated for the data; both arrays share the same memory.

Use Case: Use a view when you want to create a "window" into the original array without copying the data.
'''

# Original array
arr2 = np.array([1, 2, 3, 4])

# Create a view
arr2_view = arr2.view()

# Modify the view
arr2_view[0] = 10

print("Original array:", arr2)  # [10 2 3 4]
print("View array:", arr2_view)  # [10 2 3 4]



'''

    Difference b/w Copy and View

| Aspect         | Copy                          | View                          |
|----------------|-------------------------------|-------------------------------|
| Data Sharing   | No data sharing; independent. | Shares data with the original.|
| Memory         | Allocates new memory.         | Uses the same memory.         |
| Changes        | Changes don’t affect original.| Changes affect original.      |


'''


# How to check if an array is copy or view

# 1) if .base is None ---> Copy
# 2) if .base is not None ---> View

arr3 = np.array([1, 2, 3, 4])

# Create a copy
arr3_copy = arr3.copy()

# Create a view
arr3_view = arr3.view()

print("Copy's base:", arr3_copy.base)  # None
print("View's base:", arr3_view.base)  # Original array