number = int(input())
number_list = input().split()
a1 = set()

for i in range(number):
    a1.add(eval(number_list[i]))

if len(a1) == len(number_list):
    print("1")
else:
    print("0")
