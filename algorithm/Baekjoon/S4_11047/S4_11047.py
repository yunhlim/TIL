def recur(cur, price, total_cnt):
    if not price:
        print(total_cnt)
        exit()
    
    cnt = price // arr[cur]
    if cnt:
        recur(cur - 1, price - cnt * arr[cur], total_cnt + cnt)
    else:
        recur(cur - 1, price, total_cnt)

n, k = map(int, input().split())
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())
recur(n - 1, k, 0)