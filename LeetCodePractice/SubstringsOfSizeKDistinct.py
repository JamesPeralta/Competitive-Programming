s = input("Plaese input a string: ")
k = int(input("Please input a integer k: "))

string_length = len(s)
output = []
output_dict = {}

# Check if string is smaller than k
if string_length < k:
    print([])
else:
    start = 0
    while (start + k) <= string_length:
        char_dict = {}
        char_string = ""
        char_length = k
        for i in range(start, start + k):
            # Char is already in the hashmap
            if char_dict.get(s[i], False) is True:
                break
            else:
                char_dict[s[i]] = True
                char_string = char_string + s[i]
                char_length -= 1

        # Add this if it is distinct in characters and distinct in output
        if char_length == 0 and output_dict.get(char_string, False) is False:
            output_dict[char_string] = True
            output.append(char_string)

        start += 1


print(output)
