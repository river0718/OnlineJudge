data = input().split()
ans = 0

for i in range(len(data)):
    ans = ans + pow(int(data[i]), 3)
print(ans)
