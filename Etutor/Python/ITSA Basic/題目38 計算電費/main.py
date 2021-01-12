data = int(input())
summer = [2.10, 3.02, 4.39, 4.97, 5.63]
winter = [2.10, 2.68, 3.61, 4.01, 4.50]
index = -1

if data < 120:
    summer_pay = data * summer[0]
    winter_pay = data * winter[0]

elif 120 < data <= 330:
    summer_pay = 120 * summer[0] + (data - 120) * summer[1]
    winter_pay = 120 * winter[0] + (data - 120) * winter[1]

elif 330 < data <= 500:
    summer_pay = 120 * summer[0] + 210 * summer[1] + (data - 330) * summer[2]
    winter_pay = 120 * winter[0] + 210 * winter[1] + (data - 330) * winter[2]

elif 500 < data <= 700:
    summer_pay = 120 * summer[0] + 210 * summer[1] + 170 * summer[2] + (data - 500) * summer[3]
    winter_pay = 120 * winter[0] + 210 * winter[1] + 170 * winter[2] + (data - 500) * winter[3]

else:
    summer_pay = 120 * summer[0] + 210 * summer[1] + 170 * summer[2] + 200 * summer[3] + (data - 700) * summer[4]
    winter_pay = 120 * winter[0] + 210 * winter[1] + 170 * winter[2] + 200 * winter[3] + (data - 700) * winter[4]

summer_pay = round(summer_pay, 2)
winter_pay = round(winter_pay, 2)

print("Summer months:{:.2f}".format(summer_pay))
print("Non-Summer months:{:.2f}".format(winter_pay))
