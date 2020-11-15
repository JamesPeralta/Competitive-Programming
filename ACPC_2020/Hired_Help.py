arg = input().split()
m = int(arg[0])
k = int(arg[1])
deadlines = list(map(lambda x: int(x), input().split()))
deadlines = sorted(deadlines)

left = 0
count = 0
while left < len(deadlines):
    if deadlines[left] == -1:
        left += 1
    else:
        right = left + 1
        found = 1
        avoid = deadlines[left]
        while right < len(deadlines) and found < k:
            if deadlines[right] == -1 or deadlines[right] == avoid:
                right += 1
            else:
                avoid = deadlines[right]
                deadlines[right] = -1
                found += 1
                right += 1

        if found == k:
            count += 1

        left += 1


print(count)