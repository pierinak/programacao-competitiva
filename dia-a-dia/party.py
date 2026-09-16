import re
from collections import deque

results = []

while True:
    n = int(input())

    if n == 0:
        break

    numbers = []

    while len(numbers) < 2 * n:
        line = input()
        numbers.extend(map(int, re.findall(r"-?\d+", line)))

    graph = [[] for _ in range(1001)]

    for i in range(0, 2 * n, 2):
        x = numbers[i]
        y = numbers[i + 1]

        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * 1001
    queue = deque([1])
    visited[1] = True
    total = 0

    while queue:
        person = queue.popleft()
        total += 1

        for neighbor in graph[person]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    results.append(str(total))

print("\n".join(results))