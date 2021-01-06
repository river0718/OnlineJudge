data = input()

locate = 0
length = 0
max_length = 0
max_length_data = 10

start = 0
end = 0

for i in range(len(data)):
    if data[locate] == data[i]:
        length = length + 1
    else:
        if max_length < length:
            max_length = length
            start = locate
            end = locate + max_length
            max_length_data = data[locate]
        elif max_length == length and int(max_length_data) > int(data[locate]):
            max_length_data = data[locate]
            start = locate
            end = locate + max_length
        length = 1
        locate = i

if max_length < length:
    max_length = length
    start = locate
    end = locate + max_length
    max_length_data = data[locate]
elif max_length == length and int(max_length_data) > int(data[locate]):
    max_length_data = data[locate]
    start = locate
    end = locate + max_length

print(data[start:end])
