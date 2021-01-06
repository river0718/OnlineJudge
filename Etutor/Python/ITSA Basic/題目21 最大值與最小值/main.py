num = input().split()
maximum = float(num[0])
minimum = float(num[0])

for i in range(1, len(num)):
    if float(num[i]) > maximum:
        maximum = float(num[i])
    if float(num[i]) < minimum:
        minimum = float(num[i])

print("maximum:{:.2f}".format(maximum))
print("minimum:{:.2f}".format(minimum))
