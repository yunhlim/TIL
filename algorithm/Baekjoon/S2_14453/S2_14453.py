import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + [input().rstrip() for _ in range(n)]
prefix = [[0, 0, 0] for _ in range(n + 1)]  # P, H, S

for i in range(1, n + 1):
    if arr[i] == 'P':
        prefix[i][0] += 1
    elif arr[i] == 'H':
        prefix[i][1] += 1
    else:
        prefix[i][2] += 1
    for j in range(3):
        prefix[i][j] += prefix[i - 1][j]

result = 0
for i in range(1, n + 1):
    for j in range(3):
        for k in range(3):
            if j != k:
                result = max(result, prefix[i][j] + prefix[-1][k] - prefix[i][k])
print(result)