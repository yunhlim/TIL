import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    que = deque()
    visited = [[0] * n * 2 for _ in range(n)]   # 방문 표시
    # 시작점
    visited[0][0] = 1
    visited[0][1] = 1
    que.append([0, 1])

    while que:
        x, y = que.popleft()


n = int(input())
graph = [[0] * n * 2 for _ in range(n)]
# 타일을 담아주는 방법
for i in range(n):
    for j in range(n - i % 2):
        t1, t2 = map(int, input().split())
        graph[i][2 * j + i % 2] = t1
        graph[i][2 * j + 1 + i % 2] = t2
