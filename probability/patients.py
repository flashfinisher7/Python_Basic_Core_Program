"""
@Author: Anil
@Date: 2021-10-02 10:00
@Last Modified by: Anil
@Last Modified time: 2021-10-02 10:05
@Title :  In a particular pain clinic, 10% of patients are prescribed narcotic pain killers. Overall,
five percent of the clinic’s patients are addicted to narcotics (including pain killers and illegal
substances). Out of all the people prescribed pain pills, 8% are addicts. If a patient is an addict,
write a program to find the probability that they will be prescribed pain pills?
"""
probability_prescribenarco=1/100
probability_addict=5/100
probability_prescribenarcoaddict=8/100 
probability=(probability_prescribenarcoaddict*probability_prescribenarco)/probability_addict
print('If a patient is an addict, the probability that they will be prescribed pain pills is {}'.format(probability))