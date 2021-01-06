def round_up(input_num):
    number = [0, 0]
    int_number = int(str(input_num).split(".")[0])
    number[0] = str(input_num).split(".")[1][0:1]
    number[1] = str(input_num).split(".")[1][1:2]

    if number[1] != '' and int(number[1]) >= 5:
        number[0] = int(number[0]) + 1
        if int(number[0]) >= 10:
            number[0] = int(number[0]) - 10
            int_number = int(input_num) + 1

    return str(int_number) + "." + str(number[0])


celsius = float(input())
fahrenheit = celsius * (9 / 5) + 32

print(round_up(fahrenheit))
