number = input().split(" ")

x = int(number[0])
y = int(number[1])
z = int(number[2])

if x + y > z and x + z > y and y + z > x:
    if (x * x) + (y * y) == (z * z):
        print("Right Triangle")
    elif (x * x) + (y * y) <= (z * z):
        print("Obtuse Triangle")
    elif (x * x) + (y * y) >= (z * z):
        print("Acute Triangle")
else:
    print("Not Triangle")
