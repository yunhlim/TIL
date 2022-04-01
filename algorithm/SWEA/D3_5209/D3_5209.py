def recur(cur, total):  # 중복 없는 순열
    global min_total
    if total > min_total:   # 가지치기
        return
    if cur == n:
        min_total = min(min_total, total)
        return
    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        recur(cur + 1, total + arr[cur][i])
        visited[i] = 0


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]     # 방문 표시
    min_total = 100 * n
    recur(0, 0)
    print(f'#{tc} {min_total}')