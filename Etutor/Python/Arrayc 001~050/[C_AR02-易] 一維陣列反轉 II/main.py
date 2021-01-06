data = input().split()

for i in range(len(data), 1, -1):
    print(data[i - 1], end=" ")
print(data[0])
