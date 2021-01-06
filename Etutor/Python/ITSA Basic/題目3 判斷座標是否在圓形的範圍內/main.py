from math import *

number = input().split(" ")
x = int(number[0])
y = int(number[1])
ans = sqrt((x * x) + (y * y))

if int(ans) <= 100:
    print("inside")
else:
    print("outside")
