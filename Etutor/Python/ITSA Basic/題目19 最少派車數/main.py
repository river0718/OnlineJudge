times = int(input())
max = 0
hour = [0] * 24
inline = input().strip().split()
index = 0

for i in range(times):
    for j in range(int(inline[index]), int(inline[index + 1]), 1):
        hour[j] = hour[j] + 1
    index = index + 2

for i in range(24):
    if hour[i] > max:
        max = hour[i]

print(max)
