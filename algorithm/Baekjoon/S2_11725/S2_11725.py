from collections import deque


n = int(input())
arr = [[] for _ in range(n + 1)]

for i in range(n - 1):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

par = [0 for _ in range(n + 1)]

queue = deque()
queue.append(1)
par[1] = -1
while queue:
    v = queue.popleft()
    for v2 in arr[v]:
        if par[v2] == 0:
            queue.append(v2)
            par[v2] = v

for i in range(2, n + 1):
    print(par[i])