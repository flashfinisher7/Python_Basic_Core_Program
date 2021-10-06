"""
@Author: Anil
@Date: 2021-10-06 11:25
@Last Modified by: Anil
@Last Modified time: 2021-10-06 11:33
@Title : program to save a NumPy array to a text file
"""
import numpy as np
import os
x = np.arange(12).reshape(4, 3)
print("Original array:")
print(x)
header = 'col1 col2 col3'
np.savetxt('temp.txt', x, fmt="%d", header=header) 
print("After loading, content of the text file:")
result = np.loadtxt('temp.txt')
print(result)