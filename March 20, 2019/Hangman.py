answer = input()
guesses = input()

answer_Array = []
i = 0
for char in answer:
    if char not in answer_Array:
        answer_Array.append(char)

for guess in guesses:
    if guess in answer_Array:
        answer_Array.remove(guess)
        if len(answer_Array) == 0:
            print("WIN")
            break
    else:
        i = i + 1
        if i >= 10:
            print("LOSE")
            break

