def check(x):
    total = 0
    for i in range(n):
        total += max(0, arr[i] - x)     # 음수일 땐 0으로!
    return total >= m                   # 가능한지 확인

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e =  1_000_000_000
ans = 0
while s <= e:
    mid = (s + e) // 2
    if check(mid):          # 가능하면 mid 왼쪽을 날린다.
        ans = mid
        s = mid + 1
    else:                   # 불가능하면 mid 오른쪽을 날린다.
        e = mid - 1
print(ans)