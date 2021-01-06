def f91(number):
    if number <= 100:
        number = f91(f91(number + 11))
    elif number >= 101:
        number = number - 10
    return number


lines = int(input())
test_number = input().split(" ")

for i in range(lines):
    print(f91(int(test_number[i])))
