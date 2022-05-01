def recur(cur, total, prv):
    global max_total
    if cur == n:
        max_total = max(max_total, total)
        return
    
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        if cur:
            recur(cur + 1, total + abs(prv - arr[i]), arr[i])
        else:
            recur(cur + 1, total, arr[i])
        visited[i] = 0


n = int(input())
arr = list(map(int, input().split()))
visited = [0 for _ in range(n)]
max_total = 0
recur(0, 0, 0)
print(max_total)