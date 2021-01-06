number = int(input())
ans = int(1)

while number != 1:
    ans = ans * number
    number = number - 1

print(ans)
