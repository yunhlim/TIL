def recur(cur, cnt):
    if cnt == m:
        print(*arr)
        return
    elif cur == n:
        return

    arr[cnt] = cur + 1
    recur(cur + 1, cnt + 1)   
    recur(cur + 1, cnt)
    

n, m = map(int, input().split())
arr = [0 for _ in range(m)]

recur(0, 0)