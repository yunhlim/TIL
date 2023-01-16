n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

rnk = [1 for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rnk[i] += 1
        elif arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            rnk[j] += 1

print(*rnk)