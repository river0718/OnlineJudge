coin_of_one, coin_of_five, coin_of_fifty = 0, 0, 0
money, apple, orange, peach = map(int, input().split(","))
total_money = apple * 15 + orange * 20 + peach * 30

if total_money > money:
    print(0)
else:
    money = money - total_money
    coin_of_fifty = money // 50
    money = money - coin_of_fifty * 50

    coin_of_five = money // 5
    money = money - coin_of_five * 5

    print(str(money) + "," + str(coin_of_five) + "," + str(coin_of_fifty))
