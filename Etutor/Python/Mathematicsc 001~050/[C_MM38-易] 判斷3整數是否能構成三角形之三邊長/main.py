while True:
    number = input().split(" ")
    a = int(number[0])
    b = int(number[1])
    c = int(number[2])
    if a + b > c and a + c > b and b + c > a:
        print("fit")
    else:
        print("unfit")
