def moving(d, y, x, cnt):       # 움직이기
    ny = y + dy[d]
    nx = x + dx[d]
    if 0 <= ny < n and 0 <= nx < n and visited[arr[ny][nx]] == 0:
        visited[arr[ny][nx]] = 1        # 방문 표시
        recur(d, ny, nx, cnt + 1, 1)
        visited[arr[ny][nx]] = 0        # 재귀를 빠져 나오면 방문 표시 제거


def recur(cur, y, x, cnt, move):
    global max_cnt
    if cur == 3 and i == y:             # 사각형 완성했을 때
        max_cnt = max(max_cnt, cnt)     # 최댓값 업데이트
        return
    if cur == 2 and max_cnt > cnt * 2:  # 가지치기 두 변의 길이가 현재 값보다 작으면 return
        return
    if cur == 2 and i + j == y + x:     # 두 변을 그린 후부터는 변의 길이에 맞춰 잇는다.
        recur(cur + 1, y, x, cnt, 0)    # 마지막 세번째 꺾고 시작점으로 잇는다.
        return
    # 가던 방향으로 움직인다.
    moving(cur, y, x, cnt)
    # 방향 전환 - 2번까지 임의로 꺾고 3번부터는 사각형을 그리니 임의로 꺾지 않는다.
    if cur < 2 and move:    # 한 번이라도 움직였을 때 꺾는다.
        recur(cur + 1, y, x, cnt, 0)


dy = [1, 1, -1, -1]     # 움직일 순서 : 오른쪽 아래, 왼쪽 아래, 왼쪽 위, 오른쪽 위
dx = [1, -1, -1, 1]
for tc in range(1, 1 + int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(101)]       # 중복 확인하기 위함
    max_cnt = 0                             # 출력할 결과

    for i in range(n):          # 모든 점에서 start
        for j in range(n):
            recur(0, i, j, 0, 0)

    if max_cnt == 0:            # 사각형을 그릴 수 없으면 -1 출력
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max_cnt}')
