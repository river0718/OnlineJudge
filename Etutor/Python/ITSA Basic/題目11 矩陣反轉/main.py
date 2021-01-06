while True:
    data = input().split(" ")
    n1 = int(data[0])
    n2 = int(data[1])
    N = [[0] * n2 for i in range(n1)]

    for i in range(n1):
        N[i] = input().strip().split(" ")

    for i in range(n2):
        for j in range(n1 - 1):
            print(N[j][i], end=" ")
        print(N[n1 - 1][i])
