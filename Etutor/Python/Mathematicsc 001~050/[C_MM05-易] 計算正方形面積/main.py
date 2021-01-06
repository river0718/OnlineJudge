number = float(input())

area = str(number * number).split(".")
after_point = area[1]

if len(after_point) > 1 and int(after_point[1]) >= 5:
    after_point = str(int(after_point) + 10)

print(area[0] + "." + after_point[0])
