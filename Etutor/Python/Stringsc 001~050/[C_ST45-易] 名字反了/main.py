number = int(input())

for i in range(number):
    name = input().strip()
    d_name = name[::-1]
    d_name = d_name.lower()

    print(d_name[0].upper() + d_name[1:])
