def check(x):
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, x // i)
    return cnt >= k

n = int(input())
k = int(input())

s, e = 1, n * n
ans = 0
while s <= e:
    mid = (s + e) // 2
    if check(mid):
        e = mid - 1
        ans = mid
    else:
        s = mid + 1
print(ans)