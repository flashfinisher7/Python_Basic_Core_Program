"""
@Author: Anil
@Date: 2021-10-02 01:15
@Last Modified by: Anil
@Last Modified time: 2021-10-02 01:30
@Title :  A radar unit is used to measure speeds of cars on a motorway. The speeds are
normally distributed with a mean of 90 km/hr and a standard deviation of 10 km/hr. Write a
program to find the probability that a car picked at random is travelling at more than 100 km/hr?
"""
from statistics import NormalDist
std=NormalDist(90,10)
probability_g100=1-std.cdf(100)
print(probability_g100)