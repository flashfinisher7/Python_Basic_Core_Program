import random
class NegativeInputError(Exception):
    """Custom exception class for handling negative inputs"""
    pass
#User inputs the number of times the coin will be tossed
try:
    n_flips=int(input('Number of times the coin is tossed : '))

    if n_flips<1:
        raise NegativeInputError

    #Intiate variable that reflects the number of heads in N tosses
    head=0
    #Intiate variable that reflects the number of tails in N tosses 
    tail=0
    #Conditional to check the number of heads and tails that come after all tosses
    for x in range(1,n_flips+1):
        #pr will be 0 or 1, if 0 turns up,its heads, if 1 turns up,its tails
        pr=random.randint(0,1)
        if pr==0:
            #Increase the count of heads
            head+=1
        else:
            #increase the count of tails
            tail+=1

    #Calculating perc of head and tails in all N tosses, where N is the user input
    percentage_heads=round((head/(n_flips))*100,2)
    percentage_tails=round((tail/(n_flips))*100,2)

    #Printing the perc
    print(f"Heads:{percentage_heads}%")
    print(f"Tails:{percentage_tails}%")

except ValueError:
    print('Enter an integer value : ')
except NegativeInputError:
    print('Enter a postive integer value : ')
except Exception:
    print('Enter a valid input : ')