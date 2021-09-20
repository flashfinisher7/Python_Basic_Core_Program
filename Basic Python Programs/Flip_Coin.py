import random
num = int (input("Enter the number : "))
Head = 0
HeadPercengtage=0
Tail = 0
TailPercengtage=0
for i in range(num):
    flip=random.randint(0,1)
    if flip>=0.5:
        Head=Head+1
    else:
        Tail = Tail+1
HeadPercengtage=(Head/num)*100
TailPercengtage=(Tail/num)*100
print("Head count is : ",Head)
print("Head Percengtage is : ",HeadPercengtage)
print("Tail count is : ",Tail)
print("Tail Percengtage is : ",TailPercengtage)