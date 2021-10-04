"""
@Author: Anil
@Date: 2021-10-02 11:15
@Last Modified by: Anil
@Last Modified time: 2021-10-02 11:30
@Title : Toss a fair coin three times :
a. What is the probability of three heads, HHH?
b. What is the probability that you observe exactly one heads?
c. Given that you have observed at least one heads, what is the probability
that you observe at least two heads?
"""
from itertools import product
dataSet=set(product({'H','T'},repeat=3))
dataSet_3h={event for event in dataSet if event.count('H')==3}
dataSet_1h={event for event in dataSet if event.count('H')==1}
dataSet_m2h={event for event in dataSet if event.count('H')>=2}
def probability(data):
    return len(data)/len(dataSet)
print("Probability of three heads:",probability(dataSet_3h))
print("Probability of exactly one head:",probability(dataSet_1h))
print("Probability of morethan one head:",probability(dataSet_m2h))