number = int(input())

tw_to_other = {
    "TW": "+0000",
    "JA": "+0100",
    "USE": "-1200",
    "USC": "-1300",
    "USW": "-1400",
    "UK": "-0800"
}

other_to_tw = {
    "TW": "+0000",
    "JA": "-0100",
    "USE": "+1200",
    "USC": "+1300",
    "USW": "+1400",
    "UK": "+0800"
}

for i in range(number):
    times, country1, country2 = input().split()
    times = int(times) + int(other_to_tw[country1]) + int(tw_to_other[country2])
    if times >= 2400:
        times = times - 2400
    elif times < 0000:
        times = times + 2400

    times = str(times)
    if len(times) != 4:
        times = (4 - len(times)) * "0" + str(times)
    print(times, country2)
