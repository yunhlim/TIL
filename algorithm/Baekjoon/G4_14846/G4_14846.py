import sys
input = sys.stdin.readline

n = int(input().rstrip())
# 딕셔너리로 초기화하고 값이 있으면 값을 담아준다. 수 : 1 (일단 하나씩 들어가 있으므로)
arr = [[{}] * (n + 1)] + [[{}] + list(map(lambda x: {int(x) : 1}, input().split())) for _ in range(n)]
q = int(input().rstrip())
for i in range(1, n + 1):       # 2차원 누적합을 구한다. (1, 1) 인덱스를 기준으로 구한다.
    for j in range(1, n + 1):
        for k, v in arr[i][j - 1].items():
            arr[i][j][k] = arr[i][j].get(k, 0) + v  # key가 없으면 0에 v를 더하고 있으면 key의 개수에 v를 더한다.
        for k, v in arr[i - 1][j].items():
            arr[i][j][k] = arr[i][j].get(k, 0) + v
        for k, v in arr[i - 1][j - 1].items():
            arr[i][j][k] -= v

for _ in range(q):              # 구한 누적합을 이용해 결과를 출력한다.
    result = {}
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    for k, v in arr[x2][y2].items():
        result[k] = v
    for k, v in arr[x2][y1 - 1].items():
        result[k] -= v
    for k, v in arr[x1 - 1][y2].items():
        result[k] -= v
    for k, v in arr[x1 - 1][y1 - 1].items():
        result[k] += v
    for k, v in result.items():
        if v > 0:
            cnt += 1
    print(cnt)