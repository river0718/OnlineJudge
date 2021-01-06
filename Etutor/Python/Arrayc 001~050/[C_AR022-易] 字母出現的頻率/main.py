st = input().lower()

alphabet = [0] * 26

for i in st:
    if 97 <= ord(i) <= 122:
        alphabet[ord(i) - 97] = alphabet[ord(i) - 97] + 1

for i in range(len(alphabet)):
    if i + 1 == 26:
        print(alphabet[i])
    else:
        print(alphabet[i], end=" ")
