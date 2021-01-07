data = [int(i) for i in input().split(",")]
ans = [["000"] * data[0] for i in range(data[0])]
number = 1

if data[1] == 1:
    x, y, index = 0, -1, 0
    next_x = [0, 1, 0, -1]
    next_y = [1, 0, -1, 0]
else:
    x, y, index = -1, 0, 0
    next_x = [1, 0, -1, 0]
    next_y = [0, 1, 0, -1]

while number != data[0] ** 2 + 1:
    temp_x = x + next_x[index]
    temp_y = y + next_y[index]

    is_need_change_index = temp_x < 0 or temp_x > data[0] - 1 or temp_y < 0 or temp_y > data[0] - 1 or ans[temp_x][temp_y] != "000"
    if is_need_change_index:
        index = (index + 1) % 4

    x = x + next_x[index]
    y = y + next_y[index]

    ans[x][y] = "%03d" % number

    number = number + 1

for i in range(data[0]):
    for j in range(data[0]):
        if j + 1 == data[0]:
            print(ans[i][j])
        else:
            print(ans[i][j], end=",")
