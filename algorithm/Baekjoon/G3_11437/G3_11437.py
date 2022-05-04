from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
par = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

par[1] = 1  # 루트
que = deque()
que.append(1)
while que:
    v = que.popleft()
    for node in graph[v]:
        if par[node]:
            continue
        par[node] = v
        que.append(node)

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    arr_a = [a]
    arr_b = [b]
    while True:
        arr_a.append(par[a])
        if par[a] == 1:
            break
        a = par[a]
    while True:
        arr_b.append(par[b])
        if par[b] == 1:
            break
        b = par[b]
    arr_a = arr_a[::-1]
    arr_b = arr_b[::-1]
    result = 0
    for i in range(min(len(arr_a), len(arr_b))):
        if arr_a[i] != arr_b[i]:
            break
        result = arr_a[i]
    print(result)