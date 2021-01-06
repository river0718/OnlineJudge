number = int(input())
ans = int(0)

for i in range(1, number, 1):
    if number % i == 0:
        ans = ans + 1

if ans == 1:
    print("YES")
else:
    print("NO")
