num_loops = int(input())

journeys = []
for i in range(0, num_loops):
    journeys.append(input())


def compute_line(journey):
    backpack = []
    for i, char in enumerate(journey):
        if char in ["$", '|', '*']:
            backpack.append(char)
        elif char == 't':
            try:
                if not backpack.pop() == '|':
                    print("NO")
                    break
            except:
                y = 1


        elif char == 'j':
            try:
                if not backpack.pop() == '*':
                    print("NO")
                    break
            except:
                y = 1



        elif char == 'b':
            try:
                if not backpack.pop() == '$':
                    print("NO")
                    break
            except:
                y = 1

        if i == len(journey) - 1:
            print("YES")


for i in journeys:
    compute_line(i)
