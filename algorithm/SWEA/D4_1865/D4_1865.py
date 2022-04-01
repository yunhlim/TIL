def recur(cur, percent):
    global mmax
    if percent <= mmax:
        return
    if cur == n:
        mmax = max(mmax, percent)
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        recur(cur + 1, percent * (arr[cur][i] / 100))
        visited[i] = 0


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    mmax = 0
    recur(0, 1)
    print(f'#{tc} {mmax * 100:.6f}')