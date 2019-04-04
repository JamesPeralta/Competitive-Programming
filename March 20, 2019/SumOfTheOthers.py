from sys import stdin

for arg1 in stdin:

    arg1 = arg1[:-1]

    if arg1 == "":
        break

    all_Numbers = arg1.split(" ")
    as_Numbers = []
    for i in all_Numbers:
        as_Numbers.append(int(i))

    add = 0
    for i in as_Numbers:
        add = add + i

    print(int(add/2))
