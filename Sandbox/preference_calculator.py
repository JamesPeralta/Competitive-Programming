from collections import defaultdict
readline = "Yo"
count = defaultdict(int)
value_dict = {}
while readline != "":
    readline = input()
    parts = readline.split(",")
    if readline != "":
        parts = list(map(lambda x: x.strip(), parts))
        course = parts[2]
        points = int(parts[3])

        if course not in value_dict:
            value_dict[course] = points

        count[course] += points

min_value = 0
for elem in count:
    min_value += (count[elem] - value_dict[elem])

print(min_value)