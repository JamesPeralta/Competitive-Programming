var = input()

MAX_LIMIT = 1000000000000

num_probs, start_index = var.split(" ")
num_probs = int(num_probs)
start_index = int(start_index)

var2 = input()
problems = [int(i) for i in var2.split(" ")]

time_elapsed = problems[start_index]
problems[start_index] = MAX_LIMIT

if time_elapsed < 300:
    solved = 1
    while time_elapsed < 300:
        minimum = MAX_LIMIT
        min_index = None
        for j, i in enumerate(problems):
            if i < minimum:
                minimum = i
                min_index = j

        problems[min_index] = MAX_LIMIT
        if minimum + time_elapsed > 300:
            break
        else:
            time_elapsed = time_elapsed + minimum
            solved += 1
else:
    time_elapsed = 0
    solved = 0
print("{} {}".format(solved, time_elapsed))