def N(num):
    if num == 1:
        return 1
    else:
        return N(num - 1) * num


times = int(input())

while times != 0:
    number = int(input())
    ans = N(number)
    print(ans)

    times = times - 1
