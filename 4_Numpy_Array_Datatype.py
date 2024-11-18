# Data Types in Numpy 

'''
i - integer
b - boolean
u - unsigned integer
f - floating
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

import numpy as np

a = np.array(('apple', 'banana', 'orange'))
print(a.dtype) # it will return U6 where U is the unicode and 6 is the max length of a string


b = np.array((True, False))
print(b.dtype) # bool



# Creating array with defined datatype

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)