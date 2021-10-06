"""
@Author: Anil
@Date: 2021-10-06 12:35
@Last Modified by: Anil
@Last Modified time: 2021-10-06 12:43
@Title : program to convert a NumPy array into Python list structure
"""
import numpy as np
x= np.arange(6).reshape(3, 2)
print("Original array elements:")
print(x)
print("Array to list:")
print(x.tolist())
