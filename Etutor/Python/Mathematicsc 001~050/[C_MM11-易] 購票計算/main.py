coins = int(input())

coins_of_ten = coins // 10
coins_of_five = (coins - (coins_of_ten * 10)) // 5
coins_of_one = (coins - (coins_of_ten * 10)) % 5

print("NT10=" + str(coins_of_ten))
print("NT5=" + str(coins_of_five))
print("NT1=" + str(coins_of_one))
