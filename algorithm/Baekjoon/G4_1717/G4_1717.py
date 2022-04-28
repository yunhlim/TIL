import sys
input = sys.stdin.readline


def find(x):
    if par[x] != x:
        par[x] = find(par[x])       # 경로 압축
    return par[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if rnk[x] < rnk[y]:     # union-by-rank : 합친 횟수가 적은 쪽에서 많은 쪽으로 병합
        par[x] = y
    elif rnk[x] > rnk[y]:
        par[y] = x
    else:
        rnk[x] += 1
        par[y] = x


n, m = map(int, input().split())
par = [i for i in range(n + 1)]
rnk = [0 for _ in range(n + 1)]

for i in range(m):
    flag, a, b = map(int, input().split())
    if flag:    # 같은 집합에 포함되는지 확인
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        if find(a) != find(b):
            union(a, b)