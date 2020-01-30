word_a, word_b = input().split(" ")


a_indices = {}
for index, char in enumerate(word_a):
    data = a_indices.get(char, [])
    data.append(index)
    a_indices[char] = data

a_row = 0
b_col = 0
for index, char in enumerate(word_b):
    data = a_indices.get(char, False)
    if data is not False:
        a_row = index
        b_col = data[0]
        break

my_array = [["."] * len(word_a) for i in range(0, len(word_b))]

for i in range(0, len(word_a)):
    my_array[a_row][i] = word_a[i]

for j in range(0, len(word_b)):
    my_array[j][b_col] = word_b[j]

for row in my_array:
    print("".join(row))
