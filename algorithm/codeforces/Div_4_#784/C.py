t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(2, n):

        if arr[i % 2] % 2 != arr[i] % 2:
                print('NO')
                break
    else:
        print('YES')