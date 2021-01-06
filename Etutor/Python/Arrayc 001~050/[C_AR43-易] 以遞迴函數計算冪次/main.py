def power(n, m):
    if m == 1:
        return n
    else:
        return power(n, m - 1) * n


while True:
    number = input().split(" ")

    x = int(number[0])
    y = int(number[1])

    print(power(x, y))