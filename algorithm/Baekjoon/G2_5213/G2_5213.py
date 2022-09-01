import sys
from collections import deque
input = sys.stdin.readline


def in_range(x, y):
    return 0 <= x < n and 0 <= y < 2 * n


def bfs():
    que = deque()
    # 시작점
    visited[0][0] = 1
    visited[0][1] = 1
    que.append([0, 1])  # 큐에 좌표를 담는다.

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not in_range(nx, ny):                # 범위 확인
                continue
            # 다음 조각의 방문 순서가 더 커야 한다.
            if visited[nx][ny] > visited[x][y] + 1:
                # 다른 타일로 이동하지 않은 경우
                if ((x + y) % 2 and i == 2) or ((x + y) % 2 == 0 and i == 0):
                    que.append([nx, ny])
                    visited[nx][ny] = visited[x][y]       # 방문 순서
                # 다른 타일로 이동한 경우
                else:
                    if graph[nx][ny] == graph[x][y]:    # 인접한 두 값이 같은지 확인
                        que.append([nx, ny])
                        # 다른 타일로 이동했으니 방문 횟수를 + 1
                        visited[nx][ny] = visited[x][y] + 1
                        # 이동하면 이전 타일 값을 저장
                        tiles[find_tile_num(nx, ny)] = find_tile_num(x, y)
    cnt, tile_num = find_destination()   # 이동 횟수와 도착지의 타일 번호
    return cnt, trace_back(tile_num)        # 이동 횟수와 경로 리턴


# 타일의 순서 찾기
def find_tile_num(x, y):
    # 행 : 짝수 줄 개수 * n + 홀수 줄 개수 * (n - 1)
    cnt_x = (x // 2 + x % 2) * n + (x // 2) * (n - 1)
    # 열 : 짝수 열일 때와 홀수 열일 때 차이 : 짝수 열이면 나머지도 더해준다.
    y += 1
    cnt_y = y // 2 + (y % 2 if x % 2 == 0 else 0)
    return cnt_x + cnt_y


# 도착지 찾기
def find_destination():
    for i in range(n)[::-1]:
        for j in range(2 * n)[::-1]:
            if visited[i][j] != INF:
                # 가장 큰 타일까지 방문 횟수와 도착지 타일 번호 리턴
                return visited[i][j], find_tile_num(i, j)


# 도착점에서 출발지까지 역추적
def trace_back(num):
    ans = [num]
    while num:
        num = tiles[num]
        if not num:
            break
        ans = [num] + ans
    return ans


n = int(input())
graph = [[0] * n * 2 for _ in range(n)]
INF = n * 2 * n     # 나올 수 없는 최대 값
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]   # 우 하 좌 상
# 타일을 담아주는 방법, 짝수 열일 때와 홀수 열일 때를 구분해서 2차원 배열에 담는다.
for i in range(n):
    for j in range(n - i % 2):
        t1, t2 = map(int, input().split())
        graph[i][2 * j + i % 2] = t1
        graph[i][2 * j + 1 + i % 2] = t2

# 방문 순서 담기
visited = [[INF] * n * 2 for _ in range(n)]
tiles = [0 for _ in range(n * n)]       # 이전 타일을 저장

cnt, result = bfs()
print(cnt)
print(*result)
