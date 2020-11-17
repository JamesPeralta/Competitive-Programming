from collections import defaultdict, deque
import copy

roads = [("R", "L"), ("F", "T"), ("T", "P"), ("P", "G"), ("G", "H"), ("H", "N"), ("M", "N"), ("Y", "M"), ("R", "T"),
         ("T", "M")]

graph = defaultdict(list)
for road_one, road_two in roads:
    graph[road_one].append(road_two)
    graph[road_two].append(road_one)


def dfs(node):
    """
    :param node: Node to start from
    :return: Shortest path to H
    """

    queue = deque([(node, 0, [node])])
    visited = set(node)
    while len(queue) > 0:
        candidate, depth, path = queue.popleft()
        if candidate == "H":
            return depth, path

        for neighb in graph[candidate]:
            if neighb in visited:
                continue

            neighb_path = copy.copy(path)
            neighb_path.append(neighb)
            queue.append((neighb, depth + 1, neighb_path))

your_time, your_path = dfs("Y")
friend_time, friend_path = dfs("F")

pace = 2
if your_time * pace < friend_time:
    print("YOU WIN")
else:
    print("FRIEND WINS")
