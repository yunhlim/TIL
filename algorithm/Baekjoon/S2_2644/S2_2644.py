from collections import deque


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(m):  # 양방향으로 연결
    x, y = map(int ,input().split())
    graph[x].append(y)
    graph[y].append(x)

que = deque()
que.append(a)
visited[a] = 1

d = 0
while que:      # BFS 탐색
    sz = len(que)
    for _ in range(sz):
        v = que.popleft()
        if v == b:
            print(d)
            exit()
        for nxt in graph[v]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            que.append(nxt)
    d += 1

print(-1)