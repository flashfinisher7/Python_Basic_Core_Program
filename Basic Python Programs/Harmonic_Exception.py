try:
   number=int(input("Enter number : "))

   if number<0:
      raise Exception

except Exception:
   print('Invalid input.Please enter a positive integer')

else:
   Sum=0.0
   for x in range(1,number+1):
      Sum=Sum+(1/x)

   print(Sum)