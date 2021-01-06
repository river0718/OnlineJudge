number = input().split(" ")

x = int(number[0])
y = int(number[1])

while x != 0 and y != 0:
    if x >= y:
        x = x % y
    else:
        y = y % x

if x == 0:
    print(y)
else:
    print(x)
