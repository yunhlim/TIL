import heapq


def find_items(start):       # 현재 떨어진 위치에서 얻을 수 있는 아이템 최대 개수
    dijkstra(start)
    items_cnt = 0            # 찾을 수 있는 아이템의 수
    for i in range(1, n + 1):
        if min_d[i] != INF:
            items_cnt += items[i]
    return items_cnt


def dijkstra(start):        # 현재 위치 기준 각 정점까지의 최단 거리를 찾는다.
    min_d[start] = 0         # 현재 떨어진 위치는 거리가 0
    heap = []
    heapq.heappush(heap, [0, start])               # 현재 떨어진 위치와 거리 0을 큐에 저장
    while heap:
        d, v = heapq.heappop(heap)
        if min_d[v] != d:   # 지금 저장된 거리와 같은 경우만
            continue
        for nxt, l in graph[v]:
            if min_d[v] + l < min_d[nxt]:   # 거리가 더 작아지는 경우
                min_d[nxt] = min_d[v] + l
                heapq.heappush(heap, [min_d[nxt], nxt])   # 바뀐 값을 큐에 넣는다.


n, m, r = map(int, input().split())     # n: 지역의 개수, m: 수색 범위, r: 길의 개수
items = [0] + list(map(int, input().split())) # 각 지역의 아이템 수
graph = [[] for _ in range(n + 1)]      # 연결 관계 표시
INF = m + 1           # 수색 범위보다 큰 값을 설정
for i in range(r):
    a, b, l = map(int, input().split()) # a, b: 연결된 정점 번호, l: 길의 길이
    # 양방향 그래프
    graph[a].append([b, l])
    graph[b].append([a, l])

max_items = 0           # 가장 많이 얻을 수 있는 아이템의 개수를 찾는다.
for i in range(1, n + 1):   # 예은이는 1부터 n에 떨어질 수 있다.
    min_d = [INF for _ in range(n + 1)]       # 각 위치를 수색할 수 있는지 설정
    max_items = max(max_items, find_items(i))

print(max_items)       