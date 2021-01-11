number_of_ans = int(input())
list_of_ans = "2,"
ans = 2
temp = 2

while number_of_ans != 1:
    for i in range(2, temp):
        if i == temp - 1 and temp % i != 0:
            number_of_ans = number_of_ans - 1
            list_of_ans = list_of_ans + str(temp) + ","
            ans = ans + temp

        if temp % i == 0:
            break

    temp = temp + 1

print(list_of_ans)
print(ans)
