"""
@Author: Anil
@Date: 2021-10-05 05:00
@Last Modified by: Anil
@Last Modified time: 2021-10-05 05:13
@Title :   program to create a 8x8 matrix and fill it with a checkerboard pattern
"""
import numpy as np
x = np.ones((3,3))
print("8x8 matrix filled with Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)
