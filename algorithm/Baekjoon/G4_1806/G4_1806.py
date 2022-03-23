n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0]
INF = 100_000_001
min_len = INF

s, e = 0, 0
total = arr[e]
while e < n:
        if total >= m:
            min_len = min(min_len, e - s + 1)
        if total < m or s == e:
            e += 1
            total += arr[e]
        else:
            total -= arr[s]
            s += 1

print(0 if min_len == INF else min_len)