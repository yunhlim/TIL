# from collections import deque

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# t = int(input())
# for tc in range(1, t + 1):
#     n = int(input())
#     arr = [list(map(int, input())) for _ in range(n)]
#     visited = [[100000] * n for _ in range(n)]  # 나올 수 없는 아주 큰 값으로 초기화
#     visited[0][0] = 0
#     queue = deque()
#     queue.append((0, 0))

#     while queue:
#         x, y = queue.popleft()
#         if x == n - 1 and y == n - 1:   # 끝에 도달하면 continue
#             continue
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if visited[nx][ny] > visited[x][y] + arr[nx][ny]:   # 더 작은 값일 때
#                     visited[nx][ny] = visited[x][y] + arr[nx][ny]
#                     queue.append((nx, ny))

#     print(f'#{tc} {visited[n - 1][n - 1]}')

# 다익스트라 알고리즘
import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    INF = 100000
    dist = [[INF] * n for _ in range(n)]  # 나올 수 없는 아주 큰 값으로 초기화
    visited = [[0] * n for _ in range(n)]   # 방문 표시
    dist[0][0] = 0

    heap = []   # 힙 활용
    heap.append((0, 0, 0))
    while heap:
        d, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] > d + arr[nx][ny]:  # 경유지 갱신
                    dist[nx][ny] = d + arr[nx][ny]
                    heapq.heappush(heap, (dist[nx][ny], nx, ny))
    print(f'#{tc} {dist[-1][-1]}')