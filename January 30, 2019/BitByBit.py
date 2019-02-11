numSteps = int(input())
while numSteps != 0:
    result = ["?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?","?"]
    for i in range(0, numSteps):
        instructions = input().split(" ")
        if len(instructions) == 3:
            inst = instructions[0]
            arg1 = 31 - int(instructions[1])
            arg2 = 31 - int(instructions[2])
            #OR
            if inst == "OR":
                #There exists a 1
                if result[arg1] == "1" or result[arg2] == "1":
                    result[arg1] = "1"
                elif result[arg1] == "?" or result[arg2] == "?":
                    result[arg1] = "?"
                else:
                    result[arg1] = "0"
                
            #And
            else:
                if result[arg1] == "0" and result[arg2] == "?":
                    result[arg1] = "0"
                elif result[arg1] == "?" and result[arg2] == "0":
                    result[arg1] = "0"
                #There exists a ?
                elif result[arg1] == "?" or result[arg2] == "?":
                    result[arg1] = "?"
                #There exists a 1
                elif result[arg1] == "1" and result[arg2] == "1":
                    result[arg1] = "1"
                else:
                    result[arg1] = "0"
        else:
            inst = instructions[0]
            arg1 = 31 - int(instructions[1])
            #Clear
            if inst == "CLEAR":
                result[arg1] = "0"
            #Set
            if inst == "SET":
                result[arg1] = "1"

    finalRes = ""
    for j in result:
        finalRes = finalRes + j

    print(finalRes)

    numSteps = int(input())
