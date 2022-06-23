import heapq


def dijkstra(dir):      # dir이 0이면 x에서 각 정점까지 최단경로, dir이 1이면 각 정점에서 x까지 최단경로
    heap = [[0, x]]
    while heap:
        t, v = heapq.heappop(heap)
        if d[dir][v] != t:      # 이미 갱신된 값인 경우는 보지않는다.
            continue
        for t_nxt, nxt in graph[dir][v]:
            if d[dir][nxt] > t + t_nxt:   # 거쳐가는 경우의 시간이 더 작아질 때 바꾼다.
                d[dir][nxt] = t + t_nxt
                heapq.heappush(heap, [d[dir][nxt], nxt])


n, m, x = map(int, input().split())
graph = [[[] for _ in range(n + 1)] for _ in range(2)]  # x => 각 정점 최단경로, 각 정점 => x 최단경로
for _ in range(m):      
    s, e, t = map(int, input().split())
    graph[0][s].append([t, e])     # 시간을 앞에 적는다(heap으로 사용하기 위해)
    graph[1][e].append([t, s])     # 모든 정점에서 x까지 역방향으로 되돌아가는 걸 구하기 위해

INF = 10000000
d = [[INF for _ in range(n + 1)] for _ in range(2)]     # 2가지 다 구한다.

d[0][x], d[1][x] = 0, 0     # 시작점의 거리는 0
dijkstra(0)
dijkstra(1)

max_ans = 0
for i in range(1, n + 1):   # 두 결과를 더해 최댓값을 출력한다.
    max_ans = max(max_ans, d[0][i] + d[1][i])

print(max_ans)