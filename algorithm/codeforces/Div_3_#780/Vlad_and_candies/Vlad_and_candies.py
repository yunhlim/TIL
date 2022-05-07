t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if len(arr) == 1:
        if arr[0] == 1:
            print('YES')
        else:
            print('NO')
    elif arr[-1] - arr[-2] > 1:
        print('NO')
    else:
        print('YES')