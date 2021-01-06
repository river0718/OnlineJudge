number = int(input())
st = ""
temp = int(1)

for i in range(number):
    st = st + str(i + 1)

while temp != number:
    print(st[0:temp] + st[temp:number][::-1])
    temp = temp + 1
if number == 1:
    print(number)
