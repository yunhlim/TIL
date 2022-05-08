def in_range(x, y):     # 배열이 5x5를 넘어가는지 파악
    return 0 <= x < 5 and 0 <= y < 5


def recur(cur, cnt):    # 7명을 만들어 준다.
    if 7 - cur + cnt < 4:       # 남은 횟수를 모두 S로 뽑아도 답이 될 수 없는 경우
        return

    if cur == 7:        # 칠공주 완성
        result.add(tuple(sorted(visited)))
        return

    for x, y in visited:            # 현재 칠공주파에 속한 좌표를 찾아준다.
        for k in range(4):          # 네 방향으로 델타 탐색
            nx = x + dx[k]
            ny = y + dy[k]
            if not in_range(nx, ny) or (nx, ny) in visited:
                continue
            # 이미 확인한 S일 때
            if arr[nx][ny] == 'S' and (nx < i or (nx == i and ny < j)):  
                continue
            visited.append((nx, ny))     # 방문표시
            # S인 경우는 cnt + 1, Y면 cnt
            recur(cur + 1, cnt + 1 if arr[nx][ny] == 'S' else cnt)
            visited.pop()     # 재귀가 끝나면 방문표시 제거


arr = list(input() for _ in range(5))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = set()
for i in range(5):
    for j in range(5):
        if arr[i][j] != 'S':
            continue
        visited = [(i, j)]      # 시작점을 잡아준다.
        recur(1, 1)  # 시작점이 S인지 Y인지 파악

print(len(result))      # 될 수 있는 조합의 개수를 센다.