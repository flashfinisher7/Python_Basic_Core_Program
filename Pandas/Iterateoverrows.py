"""
@Author: Anil
@Date: 2021-10-08  10:10
@Last Modified by: Anil
@Last Modified time: 2021-10-08   10:18
@Title :  program to iterate over rows in a DataFrame.
"""
import pandas as pd
import numpy as np
exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
df = pd.DataFrame(exam_data)
for index, row in df.iterrows():
    print(row['name'], row['score'])
