def recur(cur, y, x):
    if cur == 7:                # 7번째 순열을 다 돌았을 때
        string = str(visited)   # 값을 string으로 변환
        result.add(string)      # set 자료형으로 중복 제거하여 넣어준다.
        return

    for i in range(4):          # 델타 탐색
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:     # 인덱스 초과하지 않는 범위에서
            visited[cur] = arr[ny][nx]
            recur(cur + 1, ny, nx)


dy = [0, 1, 0, -1]                      # 우 하 좌 상
dx = [1, 0, -1, 0]
for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    visited = [-1 for _ in range(7)]    # 탐색할 순열을 담는다.
    result = set()                      # 중복제거하여 값을 담아주기 위해 set 자료형 사용
    for i in range(4):                  # 초기값 세팅
        for j in range(4):
            recur(0, i, j)
    print(f'#{tc} {len(result)}')