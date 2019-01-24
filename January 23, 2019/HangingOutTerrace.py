a, b = str(input()).split(" ")
limit = int(a)
numOfEvents = int(b)
amountInside = 0
numOfRejections = 0

for i in range(0, numOfEvents):
    event, numOfPeople = str(input()).split(" ")
    if event == "enter":
            if amountInside + int(numOfPeople) > limit:
                numOfRejections += 1
            else:
                amountInside += int(numOfPeople)
    else:
            amountInside -= int(numOfPeople)

print(numOfRejections)
