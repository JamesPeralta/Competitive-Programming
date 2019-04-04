from sys import stdin

candidates = {}
for arg1 in stdin:

    arg1 = arg1[:-1]

    if arg1 == "***":
        break

    if arg1 not in candidates:
        candidates[arg1] = 1
    else:
        the_num = candidates.get(arg1)
        candidates[arg1] = the_num + 1


highest_guy = ""
highest_num = 0
current_state = "Runoff!"
for key, value in candidates.items():

    if value == highest_num:
        current_state = "Runoff!"
    elif value > highest_num:
        highest_num = value
        highest_guy = key
        current_state = highest_guy

print(current_state)
