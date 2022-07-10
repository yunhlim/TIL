n = int(input())
visited = [0 for _ in range(10)]
for i in range(1, n + 1):
    for c in str(i):
        visited[int(c)] += 1

print(*visited)
