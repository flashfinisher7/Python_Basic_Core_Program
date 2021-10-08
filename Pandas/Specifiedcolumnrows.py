"""
@Author: Anil
@Date: 2021-10-07   11:05
@Last Modified by: Anil
@Last Modified time: 2021-10-07   11:15
@Title :  program to select the specified columns and rows from a given data
frame
"""
import pandas as pd
import numpy as np

student_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

result = pd.DataFrame(student_data , index=labels)
print("Select specific columns and rows:")
print(result.iloc[[1, 3, 5, 6], [1, 3]])
