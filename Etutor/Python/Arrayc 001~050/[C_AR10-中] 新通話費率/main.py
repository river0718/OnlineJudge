money_of_month, seconds = map(int, input().split(","))
payment = [0.09, 0.08, 0.07, 0.06]
once = [0.9, 0.8, 0.7, 0.6]
twice = [0.8, 0.7, 0.6, 0.5]
money, index = 0, -1

if money_of_month == 186:
    index = 0
elif money_of_month == 386:
    index = 1
elif money_of_month == 586:
    index = 2
elif money_of_month == 986:
    index = 3

money = seconds * payment[index]

if money < money_of_month:
    money = money_of_month
elif money_of_month < money <= money_of_month * 2:
    money = money * once[index]
else:
    money = money * twice[index]

print(round(money))
