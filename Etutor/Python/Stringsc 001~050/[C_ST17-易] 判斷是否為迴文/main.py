string = input().strip()
d_string = string[::-1].strip()

if string == d_string:
    print("YES")
else:
    print("NO")
