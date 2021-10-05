"""
@Author: Anil
@Date: 2021-10-05 09:30
@Last Modified by: Anil
@Last Modified time: 2021-10-05 09:36
@Title : program to convert a list of numeric value into a one-dimensional
NumPy array
"""
import numpy as np
list = [12.23, 13.32, 100, 36.32]
print("Original List:",list)
array = np.array(list)
print("One-dimensional NumPy array is: ",array)