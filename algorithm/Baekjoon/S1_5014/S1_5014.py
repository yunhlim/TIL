# 스타트 링크

from collections import deque


def in_range(x):
    return 0 < x <= F


def bfs():
    que = deque()
    que.append(S)
    d = 0
    while que:
        sz = len(que)
        for _ in range(sz):
            node = que.popleft()
            if node == G:
                return d
            if in_range(node + U) and visited[node + U] == 0:
                visited[node + U] = 1
                que.append(node + U)
            if in_range(node - D) and visited[node - D] == 0:
                visited[node - D] = 1
                que.append(node - D)
        d += 1
    return 'use the stairs'


F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F + 1)]
print(bfs())
