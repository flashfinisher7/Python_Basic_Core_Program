"""
@Author: Anil
@Date: 2021-10-06 11:10
@Last Modified by: Anil
@Last Modified time: 2021-10-06 11:22
@Title :program compare two arrays using numpy
"""
import numpy as np
a = np.array([1, 2])
b = np.array([4, 5])
print("Array a: ",a)
print("Array b: ",b)
print("a > b")
print(np.greater(a, b))
print("a >= b")
print(np.greater_equal(a, b))
print("a < b")
print(np.less(a, b))
print("a <= b")
print(np.less_equal(a, b))