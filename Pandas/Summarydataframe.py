"""
@Author: Anil
@Date: 2021-10-07   10:30
@Last Modified by: Anil
@Last Modified time: 2021-10-07   10:42
@Title : program to display a summary of the basic information about a
specified Data Frame and its data
"""
import pandas as pd
import numpy as np

student_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

result= pd.DataFrame(student_data , index=labels)
print("Summary of the basic information about this DataFrame and its data : ")
print(result.info())