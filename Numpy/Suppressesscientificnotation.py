"""
@Author: Anil
@Date: 2021-10-06 01:15
@Last Modified by: Anil
@Last Modified time: 2021-10-06 01:20
@Title : program to suppresses the use of scientific notation for small
numbers in numpy array
"""
import numpy as np
x=np.array([1.6e-10, 1.6, 1200, .235]) 
print("Original array elements:")
print(x)
print("Print array values with precision 3:")
np.set_printoptions(suppress=True)
print(x)