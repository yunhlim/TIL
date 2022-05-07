def check():
    for i in range(n)[::-2]:
        if i == 0:
            if a[i] == sort_a[i]:
                continue
            else:
                return('NO')
        elif a[i] == sort_a[i] and a[i - 1] == sort_a[i - 1]:
            continue
        elif a[i] == sort_a[i - 1] and a[i - 1] == sort_a[i]:
            continue
        else:
            return('NO')
    return('YES')


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sort_a = sorted(a)
    print(check())