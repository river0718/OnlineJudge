number = int(input())
ans = int(0)

if number == 1:
    print("1 = 1")
else:
    for i in range(1, number, 1):
        print(str(i) + " +", end=" ")
        ans = ans + i
    print(str(number) + " = " + str(ans + number))
