def in_range(x, y):         # 범위를 만족시키는지 확인할 함수
    return 0 <= x < n and 0 <= y < m


def dfs(cur, x, y, total):  # 연결된 4개의 테트로미노 구하기
    if cur == 3:            # 4개 연결된 경우
        return total

    visited[x][y] = 1       # 연결한 좌표를 다시 탐색하지 않도록 방문표시

    ret = 0                 # 탑다운 방식으로 해결하기 위해 리턴값을 정의한다.
    for i in range(4):      # 네 방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny) and not visited[nx][ny]:
            ret = max(ret, dfs(cur + 1, nx, ny, total + arr[nx][ny]))   # 네 방향 중 최대값을 리턴한다.

    visited[x][y] = 0       # 마지막에 방문표시를 다시 지워줘야 한다.
    return ret


def purple(x, y):   # 보라색 테트로미노를 확인할 함수('ㅗ' 모양)
    nums = []       # 현재 좌표 기준 네 방향으로 존재하는 값들을 다 담아줄 리스트

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny):    # 범위를 만족한 경우 담아준다.
            nums.append(arr[nx][ny])
    
    if len(nums) >= 3:          # 길이가 3 이상인 경우만 합해서 리턴
        nums.sort(reverse=True)     # 크기가 큰 3개를 더해서 리턴
        return sum(nums[0:3])
    else:       # 길이가 3보다 작으면 0을 리턴해서 최댓값 비교해도 바뀌지 않도록 한다.
        return 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0
for i in range(n):
    for j in range(m):
        result = max(result, dfs(0, i, j, arr[i][j]), purple(i, j) + arr[i][j])

print(result)