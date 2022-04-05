# 다익스트라 알고리즘
import heapq


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


t = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
INF = 1000000000    # 나올 수 없는 큰 수
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]
    heap = [[0, 0, 0]]     # 출발점을 heap에 담는다. (연료 소비량, x, y)
    dist[0][0] = 0
    result = 0
    while heap:
        w, x, y = heapq.heappop(heap)   # 매번 최소 가중치 값을 꺼낸다.
        if x == n - 1 and y == n - 1:   # 도착점이 나오면 종료
            result = w
            break

        if w != dist[x][y]:    # 이미 나왔으면 continue
            continue

        for i in range(4):  # 네 방향 델타 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if not in_range(nx, ny):     # 범위를 만족하고 방문하지 않는 정점인 경우만
                continue
            # 높이가 높으면 연료를 더해준다. 더 낮거나 같으면 0을 더해주기 위해 max 함수 사용
            if dist[nx][ny] > w + 1 + max(0, arr[nx][ny] - arr[x][y]):
                dist[nx][ny] = w + 1 + max(0, arr[nx][ny] - arr[x][y])
                heapq.heappush(heap, [dist[nx][ny], nx, ny])    # 힙에 넣어준다.
    print(f'#{tc} {result}')