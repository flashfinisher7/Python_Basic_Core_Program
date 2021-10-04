"""
@Author: Anil
@Date: 2021-10-02 02:01
@Last Modified by: Anil
@Last Modified time: 2021-10-02 02:15
@Title :  X is a normally normally distributed variable with mean μ = 30 and standard
deviation σ = 4. Write a program to find
a. P(x < 40)
b. P(x > 21)
c. P(30 < x < 35)
"""
from statistics import NormalDist
std=NormalDist(30,4)
probability_less40=std.cdf(40)
print(probability_less40)
probability_greater21=1-std.cdf(21)
print(probability_greater21)
probability_greater30=1-std.cdf(30)
probability_less35=std.cdf(35)
probability_30to35=probability_less35-probability_greater30
print(probability_30to35)