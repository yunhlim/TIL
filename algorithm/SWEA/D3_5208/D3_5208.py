def recur(cur, change):
    global min_change
    if min_change <= change:        # 가지치기, 교환 횟수가 더 많아지면 X
        return
    if cur >= n:
        min_change = min(min_change, change)
        return
    for i in range(1, arr[cur] + 1):    # 움직일 수 있는 정류장
        recur(cur + i, change + 1)


t = int(input())
for tc in range(1, t + 1):
    arr = list(map(int, input().split()))
    n = arr.pop(0) - 1
    min_change = n
    recur(0, -1)    # 첫 정류장에서 연료를 넣고 출발하는 경우를 빼준다.
    print(f'#{tc} {min_change}')