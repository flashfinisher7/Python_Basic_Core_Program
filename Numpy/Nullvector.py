"""
@Author: Anil
@Date: 2021-10-05 10:00
@Last Modified by: Anil
@Last Modified time: 2021-10-05 10:10
@Title : Python program to create a null vector of size 10 and update sixth value to 11
"""
import numpy as np
x = np.zeros(10)
print(x)
print("Updateing seventh value to 11")
x[7] = 11
print(x)
