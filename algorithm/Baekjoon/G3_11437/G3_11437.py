from collections import deque
import sys
input = sys.stdin.readline


def lca(a, b):
    while depth[a] != depth[b]:     # depth가 같아지게
        if depth[a] > depth[b]:
            a = par[a]
        else:
            b = par[b]

    while a != b:       # 공통 조상인지 확인
        a = par[a]
        b = par[b]
    return(a)


n = int(input())
graph = [[] for _ in range(n + 1)]  # 각 노드의 연결 관계

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)      # 양방향 그래프

par = [0 for _ in range(n + 1)]     # 각 노드의 부모를 저장
depth = [0 for _ in range(n + 1)]   # 각 노드의 depth를 저장
par[1] = 1  # 루트의 부모노드는 없지만 확인됐음을 표시!!
que = deque()
que.append(1)
while que:      # bfs
    v = que.popleft()
    for node in graph[v]:
        if par[node]:       # 아직 확인되지 않는 노드인 경우만
            continue
        par[node] = v       # 루트부터 각 노드의 부모 노드를 저장
        depth[node] = depth[v] + 1      # 각 노드의 depth를 저장
        que.append(node)    # 다음 depth를 확인

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))