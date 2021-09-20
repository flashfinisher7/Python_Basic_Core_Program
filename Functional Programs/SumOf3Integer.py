"""
@Author: Anil
@Date: 2021-09-10 14:25
@Last Modified by: Anil
@Last Modified time: 2021-09-10 14:40
@Title : Sum of three Integer adds to ZERO
"""


print ("\t\t\tThis is a Sum of three Integer adds to ZERO Program\n")

print('Enter number of elements : ')
num=int(input())
l=[]
count=0
s=0
print("Enter the elements")
for a in range(num):
    a=int(input())
    l.append(a)
for i in range(len(l)):
    for j in range(1,len(l)):
        for k in range(2,len(l)):
            s=(l[i]+l[j]+l[k])
            if s==0:
                count+=1
                print(l[i],l[j],l[k])
print(count,"triplet exists")