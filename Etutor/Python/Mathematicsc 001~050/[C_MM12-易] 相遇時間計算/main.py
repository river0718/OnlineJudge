me_speed = int(100)
hua_speed = float(30 * 2.54)
total_speed = me_speed - hua_speed
far_cm = int(input()) * 100

seconds = float(far_cm / total_speed)

if str(seconds).split(".")[1][0:1] != 0:
    seconds = int(seconds) + 1

print(int(seconds))
