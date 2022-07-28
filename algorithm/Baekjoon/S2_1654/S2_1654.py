import sys
input = sys.stdin.readline

def check(x):
    result = 0
    for i in range(k):
        result += arr[i] // x
    return True if result >= n else False


k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

s = 0
e = 2 ** 31
ans = -1
while s <= e:
    mid = (s + e) // 2
    if check(mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)