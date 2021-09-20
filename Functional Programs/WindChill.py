"""
@Author: Anil
@Date: 2021-09-11 14:30
@Last Modified by: Anil
@Last Modified time: 2021-09-11 14:40
@Title : WindChill
"""
print ("\t\t\tThis is WindChill program")
def WindChill(temp, speed):
    """
    Description: we are taking WindChill as a function and passing Temp and speed as Parameter
    Parameter: temp and Speed
    temp and speed as a input
    Return: it returns Formula
    """
    return (35.74+0.6215*temp+(0.4275*temp-35.75)*speed**0.16)
temp=int(input("Enter temperature is greater then 50 : "))
speed=int(input(("Enter a speed much be greater then 120 or less than 3 : ")))
if(temp>50 and (speed>120 or speed<3)):
    print(WindChill(temp,speed))
else:
    print("PLease follow instructions while entering Temperature and speed ")