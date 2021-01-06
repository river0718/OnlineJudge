start = input().split(" ")
start_hour = int(start[0])
start_minute = int(start[1])

end = input().split(" ")
end_hour = int(end[0])
end_minute = int(end[1])

total_money = int(0)
total_minute = int((end_hour * 60 + end_minute) - (start_hour * 60 + start_minute))

if total_minute > 240:
    total_money = total_money + 120 + 160 + ((total_minute - 240) // 30) * 60
else:
    if 240 >= total_minute > 120:
        total_money = total_money + 120 + ((total_minute - 120) // 30) * 40
    else:
        total_money = total_minute // 30 * 30

print(total_money)
