"""
@Author: Anil
@Date: 2021-10-02 01:00
@Last Modified by: Anil
@Last Modified time: 2021-10-02 01:05
@Title :  Correlation between height and the pulse rate
"""
import statistics as st 
import math
x=[68,72,65,70,62,75,78,64,68]
y=[90,85,88,100,105,98,70,65,72]
mean_x=st.mean(x)
print(mean_x)
mean_y=st.mean(y)
print(mean_y)
numerator=0
denominator=0
for i in range(9):
    numerator+=(x[i]-mean_x)*(y[i]-mean_y)
    denominator+=math.sqrt(pow(x[i]-mean_x,2))*(pow(y[i]-mean_y,2))
correlation=numerator/denominator
print(correlation)
