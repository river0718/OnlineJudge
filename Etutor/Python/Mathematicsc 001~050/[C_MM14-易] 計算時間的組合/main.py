number = int(input())

days = number // (60 * 60 * 24)
number = number - (days * (60 * 60 * 24))

hours = number // (60 * 60)
number = number - (hours * (60 * 60))

minutes = number // 60
number = number - (minutes * 60)

seconds = number

print(str(days) + " days")
print(str(hours) + " hours")
print(str(minutes) + " minutes")
print(str(seconds) + " seconds")
