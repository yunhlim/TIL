from collections import deque


def bfs(x):     # bfs로 입력받은 노드에서 탐색하는 깊이 출력
    visited = [INF for _ in range(n + 1)]       # 각각의 노드에 방문한 최소 깊이를 담을 visited 배열
    que = deque()
    que.append(x)
    visited[x] = 0              # 시작한 사람의 깊이는 0
    while que:
        node = que.popleft()
        for nxt in graph[node]:
            if visited[nxt] <= visited[node] + 1:       # 더 작을 때만 업데이트
                continue
            visited[nxt] = visited[node] + 1
            que.append(nxt)
    return sum(visited[1:])

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]      # 친구 연결 관계 그래프
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)      # 양방향 그래프 연결
    graph[b].append(a)
INF = 10000

result = 0              # 케빈 베이컨 수가 작은 사람의 번호, 0으로 초기화
min_d = INF         # 케빈 베이컨 수가 작은 사람의 깊이, 큰 수로 초기화
for i in range(1, n + 1):
    depth = bfs(i)
    if min_d > depth:       # 케빈 베이컨 수가 더 작을 때 업데이트
        min_d = depth
        result = i

print(result)