def f(num):
    if num <= 1:
        return 1
    else:
        return f(num - 1) + f(num - 2)


number = int(input())
print(f(number))
