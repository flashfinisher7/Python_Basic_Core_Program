"""
@Author: Anil
@Date: 2021-10-06 11:35
@Last Modified by: Anil
@Last Modified time: 2021-10-06 11:47
@Title : program to create a contiguous flattened array
"""
import numpy as np
x = np.array([[10, 20, 30], [20, 40, 50]])
print("Original array : ")
print(x)
y = np.ravel(x)
print("New flattened array : ")
print(y)
