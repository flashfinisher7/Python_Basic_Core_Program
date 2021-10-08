"""
@Author: Anil
@Date: 2021-10-07   10:10
@Last Modified by: Anil
@Last Modified time: 2021-10-07   10:15
@Title : program to get the powers of an array values element-wise
"""
import numpy as np
x = np.arange(7)
print("Original array")
print(x)
print("First array elements raised to powers from second array, element-wise:")
print(np.power(x, 3))
