N, M = map(int, input().split())
lst = list(map(int,input().split()))

sum = 0
result = 0

for i in range(N):
    sum = lst[i]
    for j in range(i+1,N):
        if sum + lst[j] < M:
            sum += lst[j]
        else: continue
        for k in range(j+1,N):
            if sum + lst[k] <= M and result < sum + lst[k]:
                result = sum + lst[k]
        sum -= lst[j]

print(result)