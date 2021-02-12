"""

Kitten is stuck on tree that is numbered

First line is his branch
"""
from collections import defaultdict
stuck_on = int(input())

next_line = input()
graph = defaultdict(list)
while next_line != "-1":
    parsed_line = next_line.split(" ")
    parsed_line = list(map(lambda x: int(x), parsed_line))
    parent = parsed_line[0]
    for child in parsed_line[1:]:
        graph[child].append(parent)

    next_line = input()

# DFS
path = [stuck_on]

def dfs(node, path):
    if len(graph[node]) == 0:
        return True

    for neighb in graph[node]:
        path.append(neighb)
        if dfs(neighb, path):
            return True
        path.pop()

    return False

dfs(stuck_on, path)
# print(dfs(stuck_on, path))
print(" ".join([str(i) for i in path]))

