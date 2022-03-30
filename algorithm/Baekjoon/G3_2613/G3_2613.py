def check(cur, prv):
    global mid
    if cur == m - 1:
        if arr[-1] - arr[prv] <= mid:
            visited.append(n - prv)
            return True
        return False
    nxt = -1
    for i in range(prv + 1, n - m + cur + 2):
        if arr[i] - arr[prv] > mid:
            break
        nxt = i

    if nxt != -1:
        visited.append(nxt - prv)
        return check(cur + 1, nxt)

    return False

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s, e = max(arr), sum(arr)
ans = 0
while s <= e:
    visited = []
    mid = (s + e) // 2
    if check(mid):
        e = mid - 1
        ans = mid
        result = visited[:]
    else:
        s = mid + 1
print(ans)