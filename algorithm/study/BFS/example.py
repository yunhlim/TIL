from collections import deque

n = int(input())
m = int(input())
v = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

que = deque()
visited = [False for _ in range(n + 1)]

########################

# 올바른 코드
que.append(1)
visited[1] = True
while len(que) > 0:
    cur = que.popleft()

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        que.append(nxt)
        visited[nxt] = True

# 잘못된 코드
# que.append(1)
# while len(que) > 0:
#     cur = que.popleft()
#     visited[cur] = True

#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue

#         que.append(nxt)
