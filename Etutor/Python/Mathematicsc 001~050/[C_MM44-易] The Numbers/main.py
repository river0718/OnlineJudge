number = input().split(" ")
n = [0] * 2
m = [0] * 7
times = int(0)

# Input number turn array
for i in range(2):
    n[1 - i] = int(number[0]) % 10
    number[0] = int(number[0]) / 10

for i in range(7):
    m[6 - i] = int(number[1]) % 10
    number[1] = int(number[1]) / 10

# Check complete
for i in range(6):
    if m[i] == n[0] and m[i + 1] == n[1]:
        times = times + 1

print(times)
