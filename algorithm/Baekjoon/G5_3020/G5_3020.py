import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # n:동굴의 길이, m:동굴의 높이
arr_up = [0 for _ in range(m + 2)]  # 석순, 앞뒤로 padding을 넣어준다.(누적합을 위해)
arr_down = [0 for _ in range(m + 2)]  # 종유석
for i in range(n):
    height = int(input())
    if i % 2:   # 종유석, 위에서 내려온다.
        arr_up[height] += 1
    else:   # 석순, 아래서 올라온다.
        arr_down[-height-1] += 1

for i in range(1, m + 1):   # 역방향으로 누적합
    arr_up[m + 1 - i] += arr_up[m + 2 - i]
    arr_down[i] += arr_down[i - 1]

small = n
cnt = 0
for i in range(1, m + 1):
    v = arr_up[i] + arr_down[i]
    if v < small:
        small = v
        cnt = 1
    elif v == small:
        cnt += 1

print(small, cnt)