def f(n):
    if n == 1:
        return n + 1
    else:
        return f(n - 1) + f(n // 2)


number = int(input())
print(f(number))
