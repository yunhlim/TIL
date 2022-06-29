m, n = map(int, input().split())
visited = [0 for _ in range(n + 1)]     # 소수는 0이 유지된다.
visited[1] = 1      # 1은 소수가 아니다.

for i in range(2, n + 1):
    if visited[i]:
        continue
    for j in range(2 * i, n + 1, i):
        visited[j] = 1

for i in range(m, n + 1):
    if not visited[i]:
        print(i)