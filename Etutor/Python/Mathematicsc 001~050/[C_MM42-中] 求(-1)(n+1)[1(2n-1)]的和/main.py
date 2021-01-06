import math


def round_up(num):
    int_part = str(num).split(".")[0]
    float_part = str(num).split(".")[1]

    if len(float_part) > 3:
        float_part = str(num).split(".")[1][:4]
        if int(float_part[3]) >= 5:
            float_part = int(float_part[:3]) + 1

    return str(int_part + "." + str(float_part)[:3])


times = int(input())
sum = float(0.0)

for i in range(1, times + 1, 1):
    sum = sum + math.pow(-1, (i + 1)) / (2 * i - 1)

print(round_up(sum))
