from collections import deque


a, b = map(int, input().split())
visited = [-1 for _ in range(100001)]
queue = deque()
queue.append(a)
visited[a] = 0
while visited[b] == -1:
    v = queue.popleft()
    if v + 1 <= 100000 and visited[v + 1] == -1:
        visited[v + 1] = visited[v] + 1
        queue.append(v + 1)
    if v - 1 >= 0 and visited[v - 1] == -1:
        visited[v - 1] = visited[v] + 1
        queue.append(v - 1)
    if v * 2 <= 100000 and visited[v * 2] == -1:
        visited[v * 2] = visited[v] + 1
        queue.append(v * 2)

print(visited[b])
