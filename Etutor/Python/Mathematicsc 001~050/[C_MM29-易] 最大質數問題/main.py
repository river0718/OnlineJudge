number = int(input()) - 1
ans = int(number)
times = int(0)

for i in range(number, 1, -1):
    for j in range(1, number, 1):
        if number % j == 0:
            times = times + 1
    if times == 1:
        break
    else:
        number = number - 1
    times = 0

print(number)
