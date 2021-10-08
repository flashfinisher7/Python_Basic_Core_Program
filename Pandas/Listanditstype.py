"""
@Author: Anil
@Date: 2021-10-07   10:05
@Last Modified by: Anil
@Last Modified time: 2021-10-07   10:09 
@Title : program to convert a Panda module Series to Python list and it's type
"""
import pandas as pd
data = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series ")
print(data)
print(type(data))
print("Convert Pandas Series to Python list")
print(data.tolist())
print(type(data.tolist()))