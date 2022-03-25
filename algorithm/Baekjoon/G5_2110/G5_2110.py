import sys
input = sys.stdin.readline

def check(x):
    cnt = c - 1         # 시작점에 공유기를 넣는다.
    now = arr[0]        # 공유기 값은 현재 시작점
    for i in range(1, n):
        if arr[i] - now >= x:   # x보다 크거나 같은 거리만큼 떨어졌는지 확인
            cnt -= 1
            if cnt == 0:        # 공유기를 다 넣었으면 True 리턴
                return True
            now = arr[i]
    return False                # 공유기를 다 넣지 못하면 False 리턴

n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])  # 입력을 정렬한다.

ans = 0
s, e = 1, 1_000_000_000
while s <= e:               # 이진 탐색
    mid = (s + e) // 2
    if check(mid):
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)