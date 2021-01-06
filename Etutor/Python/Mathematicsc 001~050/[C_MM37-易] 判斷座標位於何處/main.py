number = input().split(" ")
x = int(number[0])
y = int(number[1])

if x == 0 and y == 0:
    print("Origin")
elif x != 0 and y == 0:
    print("x-axis")
elif x == 0 and y != 0:
    print("y-axis")
elif x > 0 and y > 0:
    print("1st Quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
elif x > 0 and y < 0:
    print("4th Quadrant")
