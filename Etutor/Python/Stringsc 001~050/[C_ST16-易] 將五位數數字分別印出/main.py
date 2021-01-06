s = input()
ls = int(len(s))
ans = ""

for i in range(ls):
    if i + 1 == ls:
        ans = ans + s[i]
    else:
        ans = ans + s[i] + "   "

print(ans)
