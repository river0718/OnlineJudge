times = int(input())
data = input().split(" ")

for i in range(0, times, 1):
    count_times = int(1)
    num = int(1)
    while num % int(data[i]) != 0:
        num = num * 10 + 1
        count_times = count_times + 1
    print(count_times)
