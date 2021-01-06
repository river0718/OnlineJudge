def round_up(num):
    int_part = str(num).split(".")[0]
    float_part = str(num).split(".")[1]

    if len(float_part) > 2:
        float_part = str(num).split(".")[1][:2]
        if int(float_part[1]) >= 5:
            float_part[0] = int(float_part[0]) + 1
            if int(float_part[0]) >= 10:
                float_part[0] = int(float_part[0]) - 10
                int_part = int(int_part) + 1

    return str(int_part + "." + float_part[0])


input_number = input().split(" ")

hours = int(input_number[0])
money = int(input_number[1])
pay_money = float(0)

if hours > 120:
    pay_money = 60 * money + 60 * (money * 1.33) + (hours - 120) * (money * 1.66)
elif 120 >= hours > 60:
    pay_money = 60 * money + (hours - 60) * (money * 1.33)
elif 60 >= hours > 0:
    pay_money = hours * money

print(round_up(pay_money))
