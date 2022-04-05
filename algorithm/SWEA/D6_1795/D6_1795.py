import heapq


def dijkstra(graph):        # 다익스트라 알고리즘, 그래프 값을 입력으로
    dp = [INF for _ in range(n + 1)]
    heap = [[0, x]]     # 출발점을 담는다.
    dp[x] = 0           # 출발 위치는 0으로
    while heap:         # 힙구조를 활용한 다익스트라 구현
        t, v = heapq.heappop(heap)      # 힙에서 걸리는 시간이 작은 값을 꺼낸다.
        if dp[v] != t:      # 확인하지 않는 정점만, 이미 확인했으면 dp 값과 다르다.
            continue
        for t2, v2 in graph[v]:     # 연결된 정점들 순회
            if dp[v2] > t + t2:     # 최소값으로 바꿔줄 수 있으면 dp 값을 바꿔주고 힙에 넣어준다.
                dp[v2] = t + t2
                heapq.heappush(heap, [dp[v2], v2])
    return dp


t = int(input())
INF = 10000000000
for tc in range(1, 1 + t):
    n, m, x = map(int, input().split())
    forward = [[] for _ in range(n + 1)]
    reverse = [[] for _ in range(n + 1)]
    for i in range(m):
        s, e, t = map(int, input().split())
        forward[s].append([t, e])   # 가중치로 정렬하기 위해 가중치, 연결된 정점 순으로 넣는다.
        reverse[e].append([t, s])
    # x에서 출발하는 최단 경로
    f_dp = dijkstra(forward)
    # x에 도착하는 최단 경로
    r_dp = dijkstra(reverse)

    max_t = 0   # 왕복 최장 시간
    for i in range(1, n + 1):   # 출발시간과 도착시간의 합이 최대일 때
        max_t = max(f_dp[i] + r_dp[i], max_t)

    print(f'#{tc} {max_t}')