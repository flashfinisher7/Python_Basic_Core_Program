"""
@Author: Anil
@Date: 2021-10-05 05:15
@Last Modified by: Anil
@Last Modified time: 2021-10-05 05:30
@Title :   program to convert a list and tuple into arrays
"""
import numpy as np
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("Before converting List to array: ")
print(np.asarray(my_list))
my_tuple = ([8, 4, 6], [1, 2, 3])
print("After converting Tuple to array: ")
print(np.asarray(my_tuple))