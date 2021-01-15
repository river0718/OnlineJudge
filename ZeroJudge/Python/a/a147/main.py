while True:
    number = int(input())

    if number == 0:
        break

    for i in range(1, number, 1):
        if i % 7 == 0:
            continue

        if i + 1 != number:
            print(i, end=" ")
        else:
            print(i)
