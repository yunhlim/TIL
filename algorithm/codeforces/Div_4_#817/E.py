t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    visited = [[0 for _ in range(1001)] for _ in range(1001)]
    for i in range(n):
        hi, wi = map(int, input().split())
        visited[hi][wi] += hi*wi
    # 2차원 누적합
    for i in range(1, 1001):
        for j in range(1, 1001):
            visited[i][j] = visited[i][j] + visited[i-1][j] + \
                visited[i][j-1] - visited[i-1][j-1]

    for i in range(q):
        hs, ws, hb, wb = map(int, input().split())
        ans = visited[hb - 1][wb - 1] - visited[hb - 1][ws] - \
            visited[hs][wb - 1] + visited[hs][ws]
        print(ans)
