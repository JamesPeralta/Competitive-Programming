def calculate(inputNum):
    X = int(inputNum)
    lst = [X]
    while X != 1:
        if X % 2 == 0:
            X = int(X / 2)
            lst.append(X)
        else:
            X = int((3 * X) + 1)
            lst.append(X)
    return lst

while True:
    inputString = input()
    if inputString == "0 0":
        break
    else:
        a, b = str(inputString).split(" ")
        aLst = calculate(int(a))
        bLst = calculate(int(b))
        intersectionBetweenBoth = set(aLst) & set(bLst)
        c = 0
        d = 0
        result = 0
        for (i, numInA) in enumerate(aLst):
            if numInA in intersectionBetweenBoth:
                c = str(i)
                result = str(numInA)
                break
        for (i, numInB) in enumerate(bLst):
            if numInB in intersectionBetweenBoth:
                d = str(i)
                break

        print (a + " needs " + c + " steps, " + b + " needs " + d + " steps, they meet at " + result)
