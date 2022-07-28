from collections import deque


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    idx_arr = [i for i in range(n)]
    zip_arr = zip(temp, idx_arr)
    rnk_arr = sorted(temp, reverse=True)
    que = deque(zip_arr)
    cnt = 0

    while que:
        rnk, idx = que.popleft()
        if rnk_arr[cnt] == rnk:
            cnt += 1
            if idx == m:
                print(cnt)
                break
            continue
        else:
            que.append((rnk, idx))