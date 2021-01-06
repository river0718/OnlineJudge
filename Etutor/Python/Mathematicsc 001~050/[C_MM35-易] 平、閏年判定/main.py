year = int(input())

is_BissextileYear = (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0)

if is_BissextileYear:
    print("Bissextile Year")
else:
    print("Common Year")
