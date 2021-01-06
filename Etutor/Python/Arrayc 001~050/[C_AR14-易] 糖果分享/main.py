times = int(input())

for i in range(times):
    n, m, L = input().split(" ")
    n = int(n)
    m = int(m)
    L = int(L)
    have_candy = [[0] * (m + 1) for p in range(n + 1)]

    for j in range(L):
        temp = input().split(" ")
        a = int(temp[0])
        b = int(temp[1])
        have_candy[a][b] = 1

        if a - 1 >= 1:
            have_candy[a - 1][b] = 1
        if a + 1 <= n:
            have_candy[a + 1][b] = 1
        if b - 1 >= 1:
            have_candy[a][b - 1] = 1
        if b + 1 <= m:
            have_candy[a][b + 1] = 1

    finish = True

    for q in range(1, n + 1):
        for w in range(1, m + 1):
            if have_candy[q][w] == 0:
                finish = False
                break

    if finish:
        print("Y")
    else:
        print("N")
