"""
@Author: Anil
@Date: 2021-10-05 05:00
@Last Modified by: Anil
@Last Modified time: 2021-10-05 05:13
@Title : program to append values to the end of an array
"""
from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Append 11 at the end of the array:")
array_num.append(11)
print("New array: "+str(array_num))
