"""
@Author: Anil
@Date: 2021-09-11 9:30
@Last Modified by: Anil
@Last Modified time: 2021-09-11 09:40
@Title : 2D Array
"""
print ("\t\t\t This is a 2DArray Program")
def Input2DArray(Number):
    """
    Description: we are taking Input2DArray as a function and passing Number as Parameter
    Parameter: Number
    Number as a input
    Return: it returns None
    """

    for i in range(2):
        for j in range(2):
             print(Number,end=" ")
        print()

Number=input("Enter a Number : ")
Input2DArray(int(Number))
Input2DArray(float(Number))
Input2DArray(bool(Number))