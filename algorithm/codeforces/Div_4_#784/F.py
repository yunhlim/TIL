t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s, e = 0, n - 1
    s_sum = arr[s]
    e_sum = arr[n - 1]
    cnt = 2
    total = 0
    while s < e:
        if s_sum == e_sum:
            total += cnt
            s_sum, e_sum = 0, 0
            cnt = 1
            s += 1
            s_sum += arr[s]
        elif s_sum > e_sum:
            cnt += 1
            e -= 1
            e_sum += arr[e]
        else:
            cnt += 1
            s += 1
            s_sum += arr[s]

    print(total)