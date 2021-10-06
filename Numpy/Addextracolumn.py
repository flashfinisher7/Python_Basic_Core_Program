"""
@Author: Anil
@Date: 2021-10-06 02:15
@Last Modified by: Anil
@Last Modified time: 2021-10-06 02:22
@Title : program to how to add an extra column to an numpy array
"""
import numpy as np
x = np.array([[10,20,30], [40,50,60]])
y = np.array([[100], [200]])
print(np.append(x, y, axis=1))