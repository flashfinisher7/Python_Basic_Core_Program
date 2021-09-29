try:
    #Enter the number of powers of 2 wanted
    number=int(input('Enter number : '))
    
except ValueError:
    print('Enter an integer value : ')
except Exception:
    print('Enter a valid input : ')

else:
    #initiating empty list
    powers=[]
    #parse through entire range and append to the empty list
    for x in range(0,number+1):
        powers.append(pow(2,x))
    print(powers)