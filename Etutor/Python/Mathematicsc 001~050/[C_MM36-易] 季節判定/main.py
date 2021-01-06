month = int(input())

isSpring = 5 >= month >= 3
isSummer = 8 >= month >= 6
isAutumn = 11 >= month >= 9
isWinter = 2 >= month >= 1 or month == 12

if isSpring:
    print("Spring")
elif isSummer:
    print("Summer")
elif isAutumn:
    print("Autumn")
elif isWinter:
    print("Winter")
