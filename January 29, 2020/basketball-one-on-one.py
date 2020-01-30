game = input()

a_score = 0
b_score = 0
current_char = ""
for index, char in enumerate(game):
    if index % 2 == 0:
        current_char = char
    else:
        if current_char == "A":
            a_score += int(char)
        else:
            b_score += int(char)

        if a_score - b_score >= 2 and a_score >= 11:
            print("A")
        elif b_score - a_score >= 2 and b_score >= 11:
            print("B")
