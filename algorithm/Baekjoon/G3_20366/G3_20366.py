def two_pointer(i, j):      # 투포인터로 차이의 최소값을 찾아준다.
    sum1 = arr[i] + arr[j]  # 조합으로 고른 i, j의 합을 구한다.
    s, e = 0, n - 1
    min_abs = 10000000000
    while s < e:
        if s in [i, j]:     # s, e가 i, j이면 건너뛴다.
            s += 1
            continue
        elif e in [i, j]:
            e -= 1
            continue
        min_abs = min(min_abs, abs(sum1 - (arr[e] + arr[s])))   # 최솟값 비교
        if arr[e] + arr[s] >= sum1:     # 크면 e를 움직인다.
            e -= 1
        else:                           # 작으면 s를 움직인다.
            s += 1
    return min_abs

n = int(input())
arr = sorted(list(map(int, input().split())))

min_result = 10000000000
for i in range(n):
    for j in range(i + 1, n):       # 조합으로 2개를 고른다.
        min_result = min(min_result, two_pointer(i, j))

print(min_result)