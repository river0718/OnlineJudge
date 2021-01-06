number = int(input())
km = str(number * 1.6).split(".")
km_after_point = km[1][0:1]

if len(km_after_point) > 1 and int(km_after_point[1]) >= 5:
    km_after_point = int(km_after_point) + 10

print(km[0] + "." + km_after_point)
