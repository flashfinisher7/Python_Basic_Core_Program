print ("\n\t\t\t\t This program is to check Leap year or not.\n")
Year = int(input("Enter a year : "))
if (Year%4)==0:
    if (Year%100)==0:
        if(Year%400)==0:
            print("{0} is a Leap Year".format(Year))
        else:
            print("{0} is not a Leap Year".format(Year))
    else:
        print("{0} is a Leap Year".format(Year))
else:
    print("{0} is not a Leap Year".format(Year))