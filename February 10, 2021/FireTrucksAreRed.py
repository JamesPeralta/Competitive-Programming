from collections import defaultdict
individuals = int(input())

common_nums = defaultdict(list)
for i in range(1, individuals + 1):
    numbers = input().split(" ")
    numbers = list(map(lambda x: int(x), numbers))
    for num in numbers:
        common_nums[num].append(i)

print(common_nums)
adj_list = defaultdict(list)
for number in common_nums.keys():
    shared_people = common_nums[number]
    for i in range(len(shared_people)):
        person_one = shared_people[i]
        for j in range(i + 1, len(shared_people)):
            person_two = shared_people[j]
            adj_list[person_one].append([person_two, number])
            adj_list[person_two].append([person_one, number])

print(adj_list)
result = []
visited = set()
stack = [1]
visited.add(1)
# print(adj_list)
while len(stack) > 0:
    candidate = stack.pop()
    for neighb, neighb_edge in adj_list[candidate]:
        if neighb in visited or neighb == candidate:
            continue
        print(candidate, neighb)
        result.append([candidate, neighb, neighb_edge])
        stack.append(neighb)
        visited.add(neighb) # Never look at a neighbor after the initial look

if len(result) == individuals - 1:
    for elem in result:
        print(" ".join([str(x) for x in elem]))
else:
    print("impossible")

"""
2 17 10 -> 1
1 5 -> 2
2 10 22 -> 3
3 17 22 9 -> 4
2 17 8 -> 5
3 9 22 16 -> 6
"""