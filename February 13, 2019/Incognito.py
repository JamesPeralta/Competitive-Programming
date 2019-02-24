num_cases = int(input())

for i in range(num_cases):
    num_attribute = int(input())
    type_to_amount = {}
    for j in range(num_attribute):
        dontcare, arg1 = str(input()).split(" ")
        if arg1 in type_to_amount:
            type_to_amount[arg1] = type_to_amount[arg1] + 1
        else:
            type_to_amount[arg1] = 1 + 1
    theTotal = 1
    for y in type_to_amount:
        theTotal = theTotal * type_to_amount[y]

    if len(type_to_amount) == 1:
        print(num_attribute)
    else:
        print(theTotal - 1)
