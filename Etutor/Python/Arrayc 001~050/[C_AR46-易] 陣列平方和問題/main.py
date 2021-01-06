number = input().split()
sum = 0.0

for i in range(len(number)):
    sum = sum + pow(float(number[i]), 2)

print("{:.6f}".format(round(sum, 6)))
