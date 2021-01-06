number = int(input())
ans = [0] * (number // 35)

for i in range(len(ans)):
    ans[i] = 35 * (i + 1)
    if i + 1 < len(ans):
        print(ans[i], end=" ")
    else:
        print(ans[i])
