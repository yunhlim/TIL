def check():        # 가능한지 체크
    for i in range(1, n + 1):       # 싸이클이 있는지 확인
        if visited[i]:              # 변호했는지 확인
            continue
        if not graph[i] or not dfs(i, 0):     # 변호안했는데 변호할 변호사가 없는 경우
            return 'NO'                     # 그리고 싸이클이 없는 경우
    return 'YES'                    # 위에서 안 걸러졌으면 가능하니 YES 출력


def dfs(node, prv):
    is_cycle = False        # 싸이클 여부
    if visited[node]:       # 변호했었으면 싸이클을 여부 : True
        return True
    visited[node] = 1       # 변호했는지 표시
    for nxt in graph[node]:
        if nxt == prv:      # 이전에 나왔던 곳으로 되돌아 가는 건 X(서로 변호하는 경우)
            continue
        if dfs(nxt, node):  # 연결된 노드들 탐색하여 cycle이 있는지 확인
            is_cycle = True
    return is_cycle


n, m = map(int, input().split())
graph = [set() for _ in range(n + 1)]      # 변호할 수 있는 변호사들의 노드 번호를 담는다.
visited = [0 for _ in range(n + 1)]     # 현재 변호사를 변호 했는지 확인
for i in range(m):
    s, e = map(int, input().split())
    graph[s].add(e)

# 양방향으로 연결된 노드들 확인
two_dir = []                        # 양방향으로 연결된 노드 관계를 담는다.
for i in range(1, n + 1):
    for v in graph[i]:
        if i not in graph[v]:       # 양방향으로 연결되지 않은 경우
            visited[v] = 1
        else:                       # 양방향으로 연결된 경우
            if i > v:               # 양방향 다 담기므로 하나만 담아준다.
                two_dir.append([i, v])

# 양방향으로 연결된 그래프를 인접리스트 형태로 변경
# 양방향 연결된 노드들 중 이미 변호된 노드가 있으면 나머지 노드도 연결한 후 양방향 그래프에는 X
graph_copy = [[] for _ in range(n + 1)]             # 양방향 연결만 확인
for a, b in two_dir:                # 양방향으로 연결된 노드들을 순회
    if visited[a] + visited[b] == 2:        # 둘 다 연결안해도 되는 경우
        continue
    elif visited[a] + visited[b] == 1:  # 하나를 연결할 수 있는 상황이면 연결한다.
        visited[a] = 1
        visited[b] = 1
    else:
        graph_copy[a].append(b)
        graph_copy[b].append(a)
graph = [graph_copy[i][:] for i in range(n + 1)]    # 양방향 연결만 확인(양쪽 다 변호되지 않은)

print(check())