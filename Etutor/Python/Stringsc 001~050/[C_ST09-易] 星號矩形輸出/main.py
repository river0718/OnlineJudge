data = input().split(" ")

n1 = int(data[0])
n2 = int(data[1])

for i in range(n2):
    for j in range(n1):
        print("*", end="")
    print("")
