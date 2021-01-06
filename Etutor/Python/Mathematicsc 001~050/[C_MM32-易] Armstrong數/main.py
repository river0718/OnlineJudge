number = int(input())

x = number // 100
y = (number - (x * 100)) // 10
z = number % 10

isArmstrong = (x * x * x) + (y * y * y) + (z * z * z) == number

if isArmstrong:
    print("Yes")
else:
    print("No")
