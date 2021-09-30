from array import *
array_num = array('i', [1, 2, 7, 3, 4, 5, 6, 7])
print("Original array: "+str(array_num))
print("Remove the first occurrence of 7 from the said array:")
array_num.remove(7)
print("New array: "+str(array_num))