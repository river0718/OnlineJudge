bank = {
    "123_456": "9000",
    "456_789": "5000",
    "789_888": "6000",
    "336_558": "10000",
    "775_666": "12000",
    "566_221": "7000"
}

times = int(input())

for i in range(times):
    account, password = input().split()
    ac = account + "_" + password
    if ac in bank:
        print(bank[ac])
    else:
        print("error")
