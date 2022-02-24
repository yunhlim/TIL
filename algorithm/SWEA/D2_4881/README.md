# [SWEA] 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합 [D2]

## 📚 문제

>NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
>
>조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.

n-queens와 비슷한 문제이다. 여기서는 visited를 열만 확인하면 되므로 1차원 count list로 표현한다.

더 최적화할 가지치기를 위해 이미 전에 구한 최소 8개의 합보다 이미 그 전 구간에서 더 큰 값이 나오면 중단하는 방식으로 경우의 수를 줄여나갔다.

그러기 위해서 min_sum을 구하고 global로 불러와 확인하면서 재귀를 진행했다.

## 📒 코드

```python
# 배열 최소 합
def recur(cur, ssum):
    global min_sum                  # 최솟값보다 현재 합이 큰지 확인하기 위해 사용
    for i in range(N):
        if visited[i] == 0:         # 나오지 않은 열의 위치일 경우
            visited[i] = 1
            ssum += arr[cur][i]
            if min_sum > ssum:      # 현재 최솟값보다 작은 경우는 종료
                if cur == N - 1:    # 다 더한 경우 최솟값인지 확인
                    min_sum = ssum
                else:
                    recur(cur + 1, ssum)    # 아직 N개가 안나왔으면 다음 열 확인
            visited[i] = 0
            ssum -= arr[cur][i]

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]     # 나왔는지 확인
    min_sum = 10 * N    # 최소 값에 가장 큰 값을 넣어 놓는다.
    recur(0, 0)     # 재귀로 해결
    print(f'#{tc} {min_sum}')

```

## 🔍 결과 : Pass