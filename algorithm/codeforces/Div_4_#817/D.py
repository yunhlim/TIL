t = int(input())
for _ in range(t):
    n = int(input())
    arr = input()
    ans = [0 for _ in range(n)]     # 각 자리 수
    for i in range(n):
        if arr[i] == 'L':
            ans[i] = i
        else:
            ans[i] = n - i - 1
    result = [0 for _ in range(n)]  # k에 따른 각 자리 수의 합
    total = sum(ans)
    k = 0
    s, e = 0, n - 1
    mid = (s + e) // 2
    while s <= e and k < n:
        if mid - s >= e - mid:
            if ans[s] == s:
                total -= ans[s]
                ans[s] = n - s - 1
                total += ans[s]
                result[k] = total
                k += 1
            s += 1
        else:
            if ans[e] == n - e - 1:
                total -= ans[e]
                ans[e] = e
                total += ans[e]
                result[k] = total
                k += 1
            e -= 1
    # 나머진 total 값을 넣어준다.
    for i in range(n)[::-1]:
        if result[i] == 0:
            result[i] = total
        else:
            break
    print(*result)
