number = int(input())
ans = int(0)

for i in range(1, number + 1, 1):
    if i % 3 == 0:
        ans = ans + i
print(ans)
