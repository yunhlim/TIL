n, k, b = map(int, input().split())
arr = [0 for _ in range(n + 1)]
for i in range(b):
    arr[int(input())] = 1

s = 1
e = k
min_cnt = 0
for i in range(s, e + 1):
    if arr[i] == 1:
        min_cnt += 1
cnt = min_cnt
while e < n:
    cnt -= arr[s]
    s += 1
    e += 1
    cnt += arr[e]
    min_cnt = min(cnt, min_cnt)

print(min_cnt)