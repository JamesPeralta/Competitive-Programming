var = input()
team_log = {}
right = "right"
wrong = "wrong"
while var != "-1":
    mins, problem_id, cont_prop = var.split(" ")
    problem_score = team_log.get(problem_id, {right: 0, wrong: 0})
    if cont_prop == right:
        problem_score[right] = int(mins)
    else:
        problem_score[wrong] = problem_score[wrong] + 20

    team_log[problem_id] = problem_score
    var = input()

problems_solved = 0
total_time = 0
for prob in team_log.keys():
    problem_score = team_log[prob]
    right_time = problem_score[right]
    wrong_time = problem_score[wrong]

    if right_time > 0:
        problems_solved += 1
    else:
        wrong_time = 0
    total_time = total_time + right_time + wrong_time

print("{} {}".format(problems_solved, total_time))