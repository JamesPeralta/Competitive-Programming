line = input()

line_arr = line.split(" ")

words = {}
output = "yes"
for word in line_arr:
    if word not in words:
        words[word] = 0
    else:
        output = "no"
        break
print(output)
