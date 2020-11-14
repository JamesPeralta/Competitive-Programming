import math

first_line = input().split()

players = int(first_line[0])
pings = int(first_line[1])

ping_arr = []
for i in range(pings):
    ping = list(map(lambda x: int(x), input().split()))
    ping_arr.append(ping)

ping_arr = sorted(ping_arr, key=lambda x: x[3])

count = 0
matches = []
seen = set()
for index, ping in enumerate(ping_arr):
    my_user_id = ping[0]
    my_x = ping[1]
    my_y = ping[2]
    my_time = ping[3]
    right = index + 1
    while right < len(ping_arr):
        their_user_id = ping_arr[right][0]
        their_x = ping_arr[right][1]
        their_y = ping_arr[right][2]
        their_time = ping_arr[right][3]

        if their_time - my_time > 10:
            break
        elif my_user_id == their_user_id:
            right += 1
            continue
        elif math.sqrt(((their_x - my_x)**2)+((their_y - my_y)**2)) <= 1000:
            match = None
            if my_user_id < their_user_id:
                match = [my_user_id, their_user_id]
            else:
                match = [their_user_id, my_user_id]
            mat = tuple(match)
            if mat not in seen:
                matches.append(match)
                count += 1
                seen.add(mat)

        right += 1

print(count)
matches = sorted(matches, key=lambda x: (x[0], x[1]))
for i in matches:
    print(f"{i[0]} {i[1]}")
