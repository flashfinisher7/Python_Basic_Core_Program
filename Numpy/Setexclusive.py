"""
@Author: Anil
@Date: 2021-10-06 10:59
@Last Modified by: Anil
@Last Modified time: 2021-10-06 11:07
@Title :program to find the set exclusive-or of two arrays
"""
import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unique values that are in only one of the input arrays:")
print(np.setxor1d(array1, array2))
