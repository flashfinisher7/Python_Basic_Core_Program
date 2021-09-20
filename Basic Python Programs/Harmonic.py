def Harmonic_Number(n):
    if(n>0 and n==1):
        return 1
    return (1/n)+Harmonic_Number(n-1)
num=int(input("Enter a Number: "))
print(Harmonic_Number(num))