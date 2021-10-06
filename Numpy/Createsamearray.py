"""
@Author: Anil
@Date: 2021-10-06 12:05
@Last Modified by: Anil
@Last Modified time: 2021-10-06 12:15
@Title :program to create an array which looks like below array
"""
import numpy as np
x = np.triu(np.arange(2, 14).reshape(4, 3), -1)
print(x)
