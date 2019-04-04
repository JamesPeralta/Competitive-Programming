arg1 = input()

for iterations in range(int(arg1)):

    welcome = "elcome to code jam"
    theArray = []
    for char in welcome:
        theArray.append(char)

    arg2 = input()
    index = 0
    final_amount = 0
    for char in arg2:
        if char == "w":
            working_with = arg2[index+1:]
            numToGo = len(working_with)
            for keepGoing in range(numToGo):
                letter_on = 0
                for theChar in working_with:
                    if theChar == theArray[letter_on]:
                        letter_on = letter_on + 1

                if letter_on == 18:
                    final_amount = final_amount + 1

                working_with = working_with[1:]

        index = index + 1

    print(final_amount)
