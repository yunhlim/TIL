import sys
input = sys.stdin.readline


def find(x):
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:      # 사이클 존재
        return True
    if rnk[x] == rnk[y]:
        rnk[x] += 1
        par[y] = x
    elif rnk[x] > rnk[y]:
        par[y] = x
    else:
        par[x] = y

    return False


n, m = map(int, input().split())
par = [i for i in range(n)]
rnk = [0 for _ in range(n)]
ans = 0
for i in range(m):
    x, y = map(int, input().split())
    if union(x, y):     # 사이클이 존재
        ans = i + 1
        break

print(ans)
