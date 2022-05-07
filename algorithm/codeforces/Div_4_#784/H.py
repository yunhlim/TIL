t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = [0 for _ in range(31)]

    for i in range(n):
        for j in range(31):
            if arr[i] & (1 << j):
                count[j] += 1
    
    result = 0
    for i in range(31)[::-1]:
        if count[i] + k >= n:
            result += 1 << i
            k -= n - count[i]
    print(result)