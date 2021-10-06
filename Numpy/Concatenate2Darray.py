"""
@Author: Anil
@Date: 2021-10-06 12:15
@Last Modified by: Anil
@Last Modified time: 2021-10-06 12:22
@Title :program to concatenate two 2-dimensional arrays
"""
import numpy as np
a = np.array([[0, 1, 3], [5, 7, 9]])
b = np.array([[0, 2, 4], [6, 8, 10]])
c = np.concatenate((a, b), 1)
print(c)
