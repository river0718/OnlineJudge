num = input()

ans = [0] * 4
for i in range(4):
    if i == 0:
        ans[2] = (int(num[0]) + 7) % 10
    elif i == 1:
        ans[3] = (int(num[1]) + 7) % 10
    elif i == 2:
        ans[0] = (int(num[2]) + 7) % 10
    else:
        ans[1] = (int(num[3]) + 7) % 10

for i in ans:
    print(i, end="")
print()
