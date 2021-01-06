number = input().split(" ")
x = int(number[0])
y = int(number[1])
temp = int(0)
ans = int(0)

# Make sure number is from small to big
if x >= y:
    temp = x
    x = y
    y = temp

while x != y + 1:
    ans = ans + x
    x = x + 1

print(ans)
