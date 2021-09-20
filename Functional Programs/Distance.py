"""
@Author: Anil
@Date: 2021-09-11 16:00
@Last Modified by: Anil
@Last Modified time: 2021-09-11 16:23
@Title : Quadratic
"""
import math
def Distance(x1,y1,x2,y2):
    """
    Description: we are taking Distance as a function and passing x1,y1,x2,y2 as Parameter
    Parameter: x1,y1,x2,y2
    x1,y1,x2,y2 as a input
    Return: it returns None
    """
    dis=((y2*y2-y1*y1)+(x2*x2-x1*x1))
    print(math.sqrt(dis))

pointX2=int(input("enter a x value of slope: "))
pointY2= int(input("Enter a y value of a slope "))
x1=0
y1=0
Distance(x1,y1,pointX2,pointY2)