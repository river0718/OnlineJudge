while True:
    data = [int(i) for i in input().split()]
    index = 0
    add = [0] * 40
    total = [0] * 40

    total[0] = data[0]

    for i in range(data[1]):
        add[i] = total[i] // 2 * 3
        total[i + 1] = add[i] + total[i]
        index = index + 1

        if i == 2:
            total[i + 1] = total[i + 1] - total[0]
        elif i > 2:
            total[i + 1] = total[i + 1] - add[i - 3]

    print(str(data[0]) + " " + str(data[1]) + " " + str(total[index]))
