times = int(input())

while times != 0:
    n, m = map(int, input().split())
    photo = [[0] * m for i in range(n)]

    # input
    for i in range(n):
        temp = input().split()
        for j in range(m):
            photo[i][j] = int(temp[j])

    # check
    for i in range(n):
        for j in range(m):
            if photo[i][j] == 0:
                print("_ ", end="")
            else:
                if i > 0 and photo[i - 1][j] == 0:
                    print("0 ", end="")
                elif i < n - 1 and photo[i + 1][j] == 0:
                    print("0 ", end="")
                elif j > 0 and photo[i][j - 1] == 0:
                    print("0 ", end="")
                elif j < m - 1 and photo[i][j + 1] == 0:
                    print("0 ", end="")
                else:
                    print("_ ", end="")

        print()

    if times - 1 != 0:
        print()

    times = times - 1
