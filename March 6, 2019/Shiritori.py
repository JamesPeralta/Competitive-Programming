arg1 = int(input())

last_letter = ''
turn = 1
fair_game = True
# For all turns
used_words = {}
last_letters = ''
for i in range(arg1):
    # Get the word
    word = input()
    # On first turn retrieve the last letter in the word
    if last_letter == '':
        last_letter = word[len(word) - 1]
        used_words[word] = i
    else:
        if last_letter == word[0] and word not in used_words:
            last_letter = word[len(word) - 1]
            used_words[word] = i
        else:
            who_lost = (i + 1) % 2

            if who_lost == 0:
                turn = 2
            else:
                turn = 1
            fair_game = False
            break

if fair_game:
    print("Fair Game")
else:
    print("Player " + str(turn) + " lost")
