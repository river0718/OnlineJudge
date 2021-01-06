minutes = int(input())
money = float(0)

if minutes >= 1500:
    money = minutes * 0.9 * 0.79
elif 1500 > minutes > 800:
    money = minutes * 0.9 * 0.9
else:
    money = minutes * 0.9

int_number = str(money).split(".")[0]
float_number = str(money).split(".")[1]

if len(float_number) >= 2:
    fln1 = int(float_number[0:1])
    fln2 = int(float_number[1:2])
    if fln2 >= 5:
        fln1 = fln1 + 1
    if fln1 >= 10:
        fln1 = fln1 - 10
        int_number = int(int_number) + 1

    money = float(float(int_number) + fln1 * 0.1)

print(money)
