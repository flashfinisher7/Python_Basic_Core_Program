"""
@Author: Anil
@Date: 2021-10-02 10:50
@Last Modified by: Anil
@Last Modified time: 2021-10-02 11:05
@Title :  Find the probability that a woman has cancer if she has a positive mammogram result?
a. One percent of women over 50 have breast cancer.
b. Ninety percent of women who have breast cancer test positive on mammograms.
c. Eight percent of women will have false positives.
"""
probability_cancer=0.01
probability_notcancer=1-probability_cancer
probability_pc=0.9
probability_ptndc=probability_pc*probability_cancer
print(probability_ptndc)
probability_ptest=(probability_ptndc)+(probability_notcancer*0.08)
print(probability_ptest)
probability_cgpt=probability_ptndc/probability_ptest
print(probability_cgpt)