t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    for j in range(m):
        cnt = 0
        s = 0
        for i in range(n):
            if arr[i][j] == 'o':
                if cnt:
                    for k in range(s, i)[::-1]:
                        if cnt:
                            arr[k][j] = '*'
                            cnt -= 1
                        else:
                            arr[k][j] = '.'
                s = i + 1
            elif arr[i][j] == '*':
                cnt += 1
        else:
            if cnt:
                for k in range(s, i + 1)[::-1]:
                    if cnt:
                        arr[k][j] = '*'
                        cnt -= 1
                    else:
                        arr[k][j] = '.'
    for i in range(n):
        print(''.join(arr[i]))