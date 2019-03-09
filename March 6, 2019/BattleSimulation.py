arg1 = str(input())

possible_combos = ["RBL", "RLB", "LRB", "LBR", "BLR", "BRL"]

final_decision = ''
i = 0
while i < len(arg1):
    if (i + 3) > len(arg1):
        if arg1[i] == 'R':
            final_decision = final_decision + 'S'
        elif arg1[i] == 'B':
            final_decision = final_decision + 'K'
        else:
            final_decision = final_decision + 'H'
        i = i + 1
        continue
    else:
        temp = arg1[i:i + 3]
        if temp in possible_combos:
            final_decision = final_decision + 'C'
            i = i + 3
        else:
            if arg1[i] == 'R':
                final_decision = final_decision + 'S'
            elif arg1[i] == 'B':
                final_decision = final_decision + 'K'
            else:
                final_decision = final_decision + 'H'
            i = i + 1

print(final_decision)
