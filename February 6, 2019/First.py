arg1 = input()

while arg1 != "0 0":
    sweetJars, sourJars = arg1.split(" ")
    sweetJarsNum = int(sweetJars)
    sourJarsNum = int(sourJars)

    if sweetJarsNum + sourJarsNum == 13:
        print('Never speak again.')
    elif sourJarsNum > sweetJarsNum:
        print('Left beehind.')
    elif sweetJarsNum > sourJarsNum:
        print('To the convention.')
    else:
        print('Undecided.')

    arg1 = input()
