data_set = set()
data = [0] * 4
number = [0] * 6

for i in range(4):
    temp = int(input())
    data[i] = temp
    data_set.add(temp)

for i in range(4):
    number[data[i] - 1] = number[data[i] - 1] + 1

long = len(data_set)

if long == 1:
    print("WIN")
elif max(number) == 2:
    ans = 0
    if number.count(2) == 2:
        for i in range(5, -1 , -1):
            if ans < i and number[i] == 2:
                ans = (i + 1) * 2
    else:
        for i in range(6):
            if number[i] == 1:
                ans = ans + (i + 1)
    print(ans)
else:
    print("R")
