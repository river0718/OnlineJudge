while True:
    num = [int(i) for i in input().split()]

    max_length = max(num)
    num[num.index(max(num))] = 0
    temp = 0

    for i in range(3):
        temp = temp + num[i]

    if temp > max_length:
        print("fit")
    else:
        print("unfit")
