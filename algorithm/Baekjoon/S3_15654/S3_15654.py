def recur(cur):
    if cur == m:
        print(*visited)
    for i in range(n):
        if arr[i] in visited:
            continue
        visited.append(arr[i])
        recur(cur + 1)
        visited.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = []
recur(0)