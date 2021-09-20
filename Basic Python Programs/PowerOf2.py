"""
@Author: Anil
@Date: 2021-09-10 14:15
@Last Modified by: Anil
@Last Modified time: 2021-09-10 14:20
@Title : power of 2
"""


print ("\t\t\tThis is a Power of Two Program\n")
print("Enter a power of 2 number :")
num=int(input())
s=set()
a=1
for i in range (num):
    a=a*2
    s.add(a)
print(s)