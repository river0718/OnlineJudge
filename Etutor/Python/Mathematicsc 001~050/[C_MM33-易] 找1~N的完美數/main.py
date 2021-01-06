def prime_number(N):
    ans = int(0)
    for j in range(1, N):
        if N % j == 0:
            ans = ans + 1

    if ans == 1:
        return True
    else:
        return False


number = int(input())
i = int(0)
times = int(2)
answer = [0] * 10
index = int(0)

while True:
    i = pow(2, times) - 1
    is_prime_number = prime_number(i)
    if is_prime_number:
        if (pow(2, times) - 1) * (pow(2, (times - 1))) > number:
            break
        answer[index] = (pow(2, times) - 1) * (pow(2, (times - 1)))
        index = index + 1
    times = times + 1

for i in range(0, index - 1, 1):
    print(answer[i], end=" ")
print(answer[index - 1])
