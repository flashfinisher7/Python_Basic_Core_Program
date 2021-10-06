"""
@Author: Anil
@Date: 2021-10-06 10:25
@Last Modified by: Anil
@Last Modified time: 2021-10-06 10:42
@Title :program to find common values between two arrays
"""
import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [10, 30, 40]
print("Array2: ",array2)
print("Common values between two arrays:")
print(np.intersect1d(array1, array2))
