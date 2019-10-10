days = int(input())
line = input()
line_arr = line.split(" ")

start = 0
high = 99
for i in range(0, len(line_arr) - 2):
    first_day = int(line_arr[i])
    third_day = int(line_arr[i + 2])
    if first_day < high and third_day < high:
        start = i
        if first_day < third_day:
            high = third_day
        else:
            high = first_day

print("{} {}".format(start + 1, high))
