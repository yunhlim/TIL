def distance(a, b):     # 경찰차가 이동한 거리
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def traceback(x, y, order):     # 경찰차 좌표를 역추적하여 어떤 경찰차가 움직였는지 찾는다.
    if x == 0 and y == 0:
        return order
    
    prv = visited[x][y]         # visited에 담은 이전 경찰차 좌표
    if prv[0] == x:
        return traceback(*prv, [2] + order)     # 이전 좌표와 경찰차 1의 위치가 같으니 경찰차 2가 움직인 것
    else:
        return traceback(*prv, [1] + order)     # 이전 좌표와 경찰차 2의 위치가 같으니 경찰차 1이 움직인 것

n = int(input())
w = int(input())
arr = [[[0, 0], [0, 0]] for _ in range(w + 1)]  # 경찰차들의 좌표를 담아준다.
arr[0][0] = [1, 1]      # 경찰차 1의 초기 위치
arr[0][1] = [n, n]      # 경찰차 2의 초기 위치
for i in range(1, w + 1):       # 경찰차가 해당 출동에 의해 움직이는 좌표
    arr[i][0] = list(map(int, input().split()))
    arr[i][1] = arr[i][0]       # 출동하는 위치는 동일(초기 위치가 다르니 2차원으로 적는 것!)

dp = [[0] * (w + 1) for _ in range(w + 1)]      # 중복을 계산을 제거하기 위해 DP 활용
visited = [[[0, 0] for _ in range(w + 1)] for _ in range(w + 1)]    # 이전 경찰차 좌표를 담아준다.(역추적 하기 위함)

# 기저조건 : 첫 출동에 의해 움직이는 거리
dp[1][0] = distance(arr[0][0], arr[1][0])       
dp[0][1] = distance(arr[0][1], arr[1][1])

for i in range(2, w + 1):
    d1 = distance(arr[i][0], arr[i-1][0])
    d2 = distance(arr[i][1], arr[i-1][1])
    for j in range(0, i):
        if j == i-1:    # 출동 횟수가 1 차이나는 경우
            dp[i][j] = 100000000
            dp[j][i] = 100000000
            for k in range(j):  # 최소의 이동거리 값을 찾는다.
                d1 = distance(arr[k][0], arr[i][0])
                d2 = distance(arr[k][1], arr[i][1])
                if dp[i][j] > dp[k][j] + d1:
                    dp[i][j] = dp[k][j] + d1    # 움직인 값을 넣어준다.
                    visited[i][j] = [k, j]      # 이전 경찰차 위치 좌표를 저장
                if dp[j][i] > dp[j][k] + d2:
                    dp[j][i] = dp[j][k] + d2
                    visited[j][i] = [j, k]
        else:       
            dp[i][j] = dp[i-1][j] + d1  # 움직인 값을 넣어준다.
            dp[j][i] = dp[j][i-1] + d2
            visited[i][j] = [i-1, j]    # 이전 경찰차 위치 좌표를 저장
            visited[j][i] = [j, i-1]

result = 10000000
index = [0, 0]
for i in range(w):      # 마지막 출동까지 끝마친 경우 중 가장 최소 이동거리를 찾는다.
    if result > dp[w][i]:
        result = dp[w][i]
        index = [w, i]
    if result > dp[i][w]:
        result = dp[i][w]
        index = [i, w]

print(result)           # 최소 이동거리를 출력한다.
for police in traceback(*index, []):        # 역추적을 통해 경찰차들의 출동 순서를 출력한다.
    print(police)