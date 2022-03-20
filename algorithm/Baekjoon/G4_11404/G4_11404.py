import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[10000000]*(n + 1) for _ in range(n + 1)]
for _ in range(m):
    s, e, fee = map(int, input().split())
    arr[s][e] = min(arr[s][e], fee)

# 플로이드 와샬 알고리즘 이용!
for k in range(1, n + 1):           # 정점을 순차적으로 수행
    for i in range(1, n + 1):
        if k == i:
            continue
        for j in range(1, n + 1):
            if k == j or i == j:    # 경유해야하니 정점이 달라야 한다.
                continue
            arr[i][j] = min(arr[i][j], arr[k][j] + arr[i][k])   # 경유할 때와 현재 값과 비교

for i in range(1, n + 1):   # 10000000을 0으로 변경
    for j in range(1, n + 1):
        if arr[i][j] == 10000000:
            arr[i][j] = 0

for i in range(1, n + 1):
    print(*arr[i][1:])