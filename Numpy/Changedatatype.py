"""
@Author: Anil
@Date: 2021-10-06 11:48
@Last Modified by: Anil
@Last Modified time: 2021-10-06 11:59
@Title : program to change the data type of an array
"""
import numpy as np
x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(x)
print("Data type of the array x is:",x.dtype)
# Change the data type of x
y = x.astype(float)
print("New Type: ",y.dtype)
print(y)
