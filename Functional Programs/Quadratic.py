"""
@Author: Anil
@Date: 2021-09-11 14:45
@Last Modified by: Anil
@Last Modified time: 2021-09-11 15:15
@Title : Quadratic
"""
import cmath
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))

delta= (b*b-(4*a*c))

root1 = (-b+(cmath.sqrt(delta)))/(2*a)
root2 = (-b-(cmath.sqrt(delta)))/(2*a)

print("Root1 of x is : ",root1)
print("Root2 of x is : ",root2)