arg1 = int(input())
arg2 = input()
arg3 = input()

# If the output is even
if arg1 % 2 == 0:
    if arg2 == arg3:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
else:
    new_word = ''
    for char in arg2:
        if char == '0':
            new_word = new_word + '1'
        else:
            new_word = new_word + '0'

    if new_word == arg3:
        print("Deletion succeeded")
    else:
        print("Deletion failed")

