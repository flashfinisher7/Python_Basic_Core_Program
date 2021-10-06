"""
@Author: Anil
@Date: 2021-10-06 12:25
@Last Modified by: Anil
@Last Modified time: 2021-10-06 12:30
@Title :program to make an array immutable
"""
import numpy as np
x = np.zeros(10)
x.flags.writeable = False
print("Test the array is read-only or not:")
print("Try to change the value of the first element:")
x[0] = 1
