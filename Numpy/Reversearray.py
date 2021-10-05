"""
@Author: Anil
@Date: 2021-10-05 09:40
@Last Modified by: Anil
@Last Modified time: 2021-10-05 09:49
@Title : program to reverse an array (first element becomes last)
"""
import numpy as np
x = np.arange(12, 38)
print("Original array:")
print(x)
print("Reverse array:")
x = x[::-1]
print(x)