from collections import defaultdict

x = input().split()
n = int(x[0])
m = int(x[1])

graph = defaultdict(list)

employee = 2
for i in range(n - 1):
    person = int(input())
    graph[person].append(employee)
    employee += 1

manages = defaultdict(set)
for employee in range(2, n - 1):
    stack = graph[employee]
    while len(stack) > 0:
        candidate = stack.pop()
        manages[employee].add(candidate)

        for elem in graph[candidate]:
            stack.append(elem)

print(manages)