num_cases = int(input())
for i in range(0, num_cases):
    number = input()
    reverse = number[::-1]

    final = ""
    found = False
    for num in reverse:
        num = int(num)
        if num - 1 >= 0 and found == False:
            final = str(num-1) + final
            found = True
        else:
            final = str(num) + final
    print(int(final))
