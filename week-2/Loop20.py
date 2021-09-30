x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

a1 = min(x, y, z)
temp = max(x, y, z)
a2 = (x + y + z) - a1 - temp
print("Numbers in sorted order: ", a1, a2, temp)