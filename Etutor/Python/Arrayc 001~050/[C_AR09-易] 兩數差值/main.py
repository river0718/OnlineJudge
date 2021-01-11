data1 = input().split(",")
data2 = data1.copy()
max_number = ""
min_number = ""

for i in range(len(data1)):

    max_number = max_number + max(data1)

    data1[data1.index(max(data1))] = "00"

for i in range(len(data2)):
    min_number = min_number + min(data2)

    data2[data2.index(min(data2))] = "99"

ans = int(max_number) - int(min_number)
print(ans)
