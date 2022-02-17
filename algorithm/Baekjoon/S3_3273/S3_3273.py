N = int(input())
arr = list(map(int, input().split()))
X = int(input())
arr.sort()
s = 0
e = N - 1
cnt = 0

while s < e:
    if arr[s] + arr[e] >= X:
        if arr[s] + arr[e] == X:
            cnt += 1
        e -= 1
    else:
        s += 1
print(cnt)