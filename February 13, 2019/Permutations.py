from string import ascii_lowercase
from itertools import permutations


def generate_combos( word ):
    combos = []
    for i in range(len(word)):
        for l in ascii_lowercase:
            combos.append( word[:i]+l+word[i+1:] )
    print(combos)


num_cases = int(input())
for i in range(0, num_cases):
    number = input()
    alphabet = []
    for num in number:
        alphabet.append(num)

    the_sum = 0
    for j in alphabet:
        the_sum = the_sum + int(j)

    the_range = the_sum - 1
    zero_n = ""
    for k in range(0, the_range):
        zero_n = zero_n + str(k)

    combinations = []
    perms = [''.join(p) for p in permutations(zero_n)]
    print(perms)
    for p in perms:
        a_number = int(p)
        if a_number <= int(number):
            combinations.append(a_number)
        # the_perm = int(p)
        # if the_perm <= the_range:
        #     combinations.append(int(p))

    print(combinations[len(combinations) - 1])
