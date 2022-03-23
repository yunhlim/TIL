import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())        # 정점과 간선의 수
INF = n * 10                            # 나올 수 있는 가장 큰 값보다 크게 설정
arr = [[] for _ in range(n + 1)]
start = int(input().rstrip())           # 시작점
dp = [0 for _ in range(n + 1)]
for _ in range(e):                      # 가중치에 관한 그래프
    a, b, w = map(int, input().split())
    arr[a].append((w, b))               # 행 -> 열 일 때 값은 가중치

dp = [INF for _ in range(n + 1)]        # 시작점에서의 최단 거리
dp[start] = 0                           # 시작점은 0이다.

heap = []
heapq.heappush(heap, (0, start))        # 시작점을 담고 시작
while heap:
    w, v = heapq.heappop(heap)
    if dp[v] != w:                      # 변경된 값과 다르면 pass
        continue
    for t_w, t_v in arr[v]:
        if dp[t_v] > t_w + w:           # 최소값으로 넣어준다.
            dp[t_v] = t_w + w
            heapq.heappush(heap,(t_w + w, t_v))

for i in range(1, n + 1):
    print('INF' if dp[i] == INF else dp[i])