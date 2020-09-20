# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict


class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = defaultdict(list)

        def dfs(node, par=None):
            if node:
                graph[node].append(par)

                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = deque(node for node in graph if node and node.val == k)
        seen = set(queue)

        # Perform BFS
        while len(queue) > 0:
            node = queue.popleft()
            seen.add(node)
            if node:
                if len(graph[node]) <= 1:
                    return node.val
                else:
                    for neigh in graph[node]:
                        if neigh not in seen:
                            queue.append(neigh)
