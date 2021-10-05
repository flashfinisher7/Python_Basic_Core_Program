"""
@Author: Anil
@Date: 2021-10-05 09:40
@Last Modified by: Anil
@Last Modified time: 2021-10-05 09:49
@Title :  program to create a 2d array with 1 on the border and 0 inside
"""
import numpy as np
x = np.ones((3,3))
print("Original array:")
print(x)
print("0 on the border and 1 inside in the array")
x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(x)
