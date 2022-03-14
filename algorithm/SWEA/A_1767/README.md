# [SWEA] 1767. [SW Test 샘플문제] 프로세서 연결하기

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf

---

**델타 탐색**과 **백트래킹**을 활용한 문제이다.

최대한 많은 코어를 연결시키고 연결된 코어가 같을 땐 연결된 전선의 길이가 가장 작은 값을 구하는 문제이다.

가장자리에 있는 코어는 사용하지 않으니 가장자리에 있지 않는 코어들의 좌표를 우선적으로 리스트에 담는다.



## recur()

재귀를 활용한 백트래킹을 적용하기 위해 cur이 늘어날수록 좌표들을 하나씩 선택한다.

cur이 좌표와 같으면 return으로 종료한다.

한 코어 당 4방향으로 탐색한다. 모두 탐색해야하므로 순열이다.



## check()

중간에 가지치기를 위해 선을 연결할 수 없는 방향인지 확인한다.

확인하기 위해 `check(y, x)`로 4가지 방향으로 연결할 수 있는지 찾고 연결할 수 있으면 연결 길이를 4개를 담은 리스트로 반환한다. 연결할 수 없으면 0을 담아 반환한다.



## connect()

연결할 방향으로 다 1로 바꾸어주는 함수이다. 

연결이 되어있으면 unconnect도 해준다. 다 0으로 바꾼다.



연결된 개수가 커질수록 result에 새로 넣어주고, 연결된 개수가 같으면 result와 비교해서 더 작으면 바꾸어준다.

연결된 개수와 길이를 같이 리스트에 담아 비교해준다.



## 📒 코드

```python
# 모든 프로세서가 가질 수 있는 경우의 수를 구한다 백트래킹!!
def check(y, x):    # 우하좌상 확인
    global n
    direction = [0, 0, 0, 0]    # 연결할 수 있으면 연결 길이 표시
    for d in range(4):
        now_y, now_x = y, x
        length = 0
        while 0 < now_y < n - 1 and 0 < now_x < n - 1:  # index 넘지 않게
            length += 1
            now_y += dy[d]
            now_x += dx[d]
            if arr[now_y][now_x]:   # 코어가 있거나 선이 있으면 break
                break
        else:
            direction[d] = length
    return direction


def connect(y, x, d):   # 선을 연결하거나 해제해준다.
    global n
    now_y, now_x = y, x
    while 0 < now_y < n - 1 and 0 < now_x < n - 1:
        now_y += dy[d]
        now_x += dx[d]
        arr[now_y][now_x] ^= 1  # 반대로 바꿔주는 비트연산자


def recur(cur, min_sum, result_cnt):    # 백트래킹
    global result
    if result_cnt > result[0]:  # 연결된 개수가 더 많으면 바꿔준다.
        result[0] = result_cnt
        result[1] = min_sum
    elif result_cnt == result[0]:   # 연결된 개수가 같으면 더 작은 것으로
        if result[1] > min_sum:
            result[1] = min_sum
    if cur == cnt:      # 선을 더 연결할 수 없으면 종료
        return
    y, x = core[cur][0], core[cur][1]   # 코어의 좌표 값
    direction = check(y, x)         # 움직일 수 있는 방향과 길이
    for d in range(4):
        if direction[d] == 0:       # 움직일 수 없는 방향은 보지 않는다.
            continue
        connect(y, x, d)        # 선을 연결
        recur(cur + 1, min_sum + direction[d], result_cnt + 1)  # 연결하고 다음으로
        connect(y, x, d)        # 선을 해제
    recur(cur + 1, min_sum, result_cnt)     # 선을 연결하지 않고 다음으로


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [0, 1, 0, -1]  # 우 하 좌 상
    dx = [1, 0, -1, 0]
    core = []   # 연결시킬 코어들의 좌표
    cnt = 0     # 연결시킬 코어의 개수
    for i in range(1, n - 1):   # 가장자리가 아닌 코어들을 담는다.
        for j in range(1, n - 1):
            if arr[i][j] == 1:
                core.append([i, j])
                cnt += 1        # 연결시킬 코어 개수
    result = [0, 0]     # 연결 개수와 총 연결 길이
    recur(0, 0, 0)      # 재귀를 돌며 가장 많은 연결 중 가장 최소의 길이를 찾는다.
    print(f'#{tc} {result[1]}')
```

## 🔍 결과 : Pass