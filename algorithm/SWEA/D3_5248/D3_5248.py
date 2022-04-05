# 연결 요소
def dfs(v):
    visited[v] = 1          # 방문 표시

    for nxt in graph[v]:    # 정점에서 연결된 정점들 순회
        if visited[nxt]:    # 방문하지 않는 정점들을 선택
            continue
        dfs(nxt)


t = int(input())
for tc in range(1, 1 + t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]  # 1번부터 n번까지

    for i in range(m):     # 무방향 그래프 연결 상태
        v1 = tmp[i * 2]
        v2 = tmp[i * 2 + 1]
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [0 for _ in range(n + 1)]
    cnt = 0

    for i in range(1, n + 1):
        if visited[i]:  # 방문 확인
            continue
        dfs(i)      # 연결 요소를 다 방문 표시
        cnt += 1    # 연결 요소의 개수 + 1

    print(f'#{tc} {cnt}')