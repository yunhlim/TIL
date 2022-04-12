def find(x):
    if par[x] != x:
        par[x] = find(par[x])   # 경로 압축
    return par[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if rnk[a] < rnk[b]:         # union-by-rank
        par[a] = b
    elif rnk[a] > rnk[b]:
        par[b] = a
    else:
        rnk[b] += 1
        par[a] = b


n = int(input())
par = [i for i in range(n + 1)]
rnk = [0 for _ in range(n + 1)]
for i in range(n - 2):
    a, b = map(int, input().split())
    union(a, b)

result = set()
for i in range(1, n + 1):
    result.add(find(i))
    if len(result) == 2:
        break
print(*result)