times = int(input())

for i in range(times):
    data = input().split()

    symbol_of_operation = data[0]
    a = int(data[1])
    ai = int(data[2])
    b = int(data[3])
    bi = int(data[4])

    if symbol_of_operation == "+":
        print(a+b, ai+bi)
    elif symbol_of_operation == "-":
        print(a-b, ai-bi)
    elif symbol_of_operation == "*":
        print(a * b - ai * bi, b * ai + a * bi)
