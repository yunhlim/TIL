def in_range(x, y):                     # 범위 넘어서는지 확인
    return 0 <= x < n and 0 <= y < m


def attack(x, y, d):
    if visited[x][y]:                   # 넘어진 도미노는 넘어뜨릴 수 없다.
        return 0
    
    visited[x][y] = 1                   # 현재 위치의 도미노는 넘어진다.
    cnt = 1
    for _ in range(arr[x][y] - 1):
        x += dx[dir[d]]
        y += dy[dir[d]]
        if not in_range(x, y):          # 범위 넘어서면 종료
            break
        cnt += attack(x, y, d)          # 다음 도미노들이 넘어지는 건 재귀로 구현
    return cnt
        

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]   # 도미노 높이
visited = [[0] * m for _ in range(n)]       # 넘어졌는지 확인, 넘어졌으면 1, 아니면 0
# 동서남북
dir = {'E': 0, 'W': 1, 'S': 2, 'N': 3}
dx = [0, 0, 1, -1]                  # 순서대로 0(E) W(1) S(2) N(3)
dy = [1, -1, 0, 0]

score = 0
for i in range(r):
    # 공격
    x, y, d = input().split()
    x, y = int(x) - 1, int(y) - 1   # 격자판이 1부터 n까지이므로 1씩 빼준다.
    score += attack(x, y, d)        # 점수를 더해준다.
    # 수비
    x, y = map(lambda x: int(x) - 1, input().split())       # 격자판이 1부터 n까지이니 1씩 뺀다.
    visited[x][y] = 0               # 눕혀져있는 걸 세워준다.

print(score)                        # 점수 출력

# 게임판 상태 출력
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:      # 세워져있는 건 S
            visited[i][j] = 'S'
        else:                       # 눕혀져있는 건 F
            visited[i][j] = 'F'

for i in range(n):                  # 게임판 상태를 출력한다.
    print(*visited[i])