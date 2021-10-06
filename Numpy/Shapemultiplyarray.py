"""
@Author: Anil
@Date: 2021-10-06 12:30
@Last Modified by: Anil
@Last Modified time: 2021-10-06 12:35
@Title :program to create an array of (3, 4) shape, multiply every element
value by 3 and display the new array
"""
import numpy as np
x= np.arange(12).reshape(3, 4)
print("Original array elements:")
print(x)
for a in np.nditer(x, op_flags=['readwrite']):
    a[...] = 3 * a
print("New array elements:")
print(x)
