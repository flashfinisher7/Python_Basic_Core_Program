"""
@Author: Anil
@Date: 2021-10-06 10:00
@Last Modified by: Anil
@Last Modified time: 2021-10-06 10:13
@Title : program to find the real and imaginary parts of an array of complex
numbers
"""
import numpy as np
x = np.sqrt([1+0j])
y = np.sqrt([0+1j])
print("Original array:x ",x)
print("Original array:y ",y)
print("Real part of the array:")
print(x.real)
print(y.real)
print("Imaginary part of the array:")
print(x.imag)
print(y.imag)
