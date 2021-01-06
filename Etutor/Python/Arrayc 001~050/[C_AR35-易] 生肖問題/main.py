Chinese_animal_sign = ["rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep", "monkey", "rooster", "dog", "pig"]

year = int(input())

if year >= 2008:
    print(Chinese_animal_sign[(year - 2008) % 12])
else:
    print(Chinese_animal_sign[-(2008 - year) % 12])
