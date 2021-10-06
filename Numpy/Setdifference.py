"""
@Author: Anil
@Date: 2021-10-06 10:45
@Last Modified by: Anil
@Last Modified time: 2021-10-06 10:57
@Title :program to find the set difference of two arrays
"""
import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unique values in array1 that are not in array2:")
print(np.setdiff1d(array1, array2))
