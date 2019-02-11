rules, times = str(input()).split(" ")
hashmap = {}
for i in range(0, int(rules)):
    x, y = str(input()).split(' -> ')
    hashmap[x] = y


starting = str(input())
newString = ""
for j in range(0, int(times)):
    for char in starting:
        if char in hashmap:
            newString = newString + hashmap[char]
        else:
            newString = newString + char
    starting = newString
    newString = ""

print(starting)
