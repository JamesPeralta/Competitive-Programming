num_temps = int(input())
temp_array = input().split(" ")

num_found = 0
for temp in temp_array:
    if int(temp) < 0:
        num_found += 1

print(num_found)