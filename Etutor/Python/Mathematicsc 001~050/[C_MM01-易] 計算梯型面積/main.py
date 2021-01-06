number = input().split()

topline = int(number[0])
baseline = int(number[1])
height = int(number[2])

print("Trapezoid area:" + str((topline + baseline) * height / 2))
