def solution(T):
    if verify_input(T) is False:
        return 0

    front_comb = check_front(T[0:2])
    back_comb = check_back(T[3:])

    return front_comb * back_comb


def verify_input(T):
    if T[0] != "?" and T[1] != "?" and T[3] != "?" and T[4] != "?":
        print("Here")
        return False

    first_char = T[0] if T[0] != '?' else '0'
    second_char = T[1] if T[0] != '?' else '0'
    third_char = T[3] if T[0] != '?' else '0'
    fourth_char = T[4] if T[0] != '?' else '0'

    asnumber = int(first_char + second_char + third_char + fourth_char)
    if asnumber > 2359:
        return False

def check_front(front):
    # Four cases
    if front[0] == '?' and front[1] == '?':
        return 24
    elif front[0] == "?":
        if int(front[1]) > 3:
            return 2
        else:
            return 3
    elif front[1] == "?":
        if int(front[0]) == 2:
            return 4
        else:
            return 10
    else:
        return 1


def check_back(back):
    if back[0] == '?' and back[1] == '?':
        return 60
    elif back[0] == "?":
        return 6
    elif back[1] == "?":
        return 10
    else:
        return 1


# T = "2?:45"
# T = "?9:32"
# T = "0?:?0"
# T = "?4:0?"
T = "29:01"
print(solution(T))