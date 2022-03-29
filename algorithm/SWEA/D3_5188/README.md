# [SWEA] 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합 [D3]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT

---

## 📖 풀이

탑다운 DP 백트래킹으로 해결했다.

(0, 0)에서 시작해 아래와 오른쪽 중 최소 값을 선택한다.

이 때 dp에 값이 저장되어 있지 않으면 재귀함수를 호출해 그 때의 최소 값을 찾는다.

기저 조건을 위해 (n - 1, n - 1) 일 때 값을 마지막에 도달했을 때의 값을 넣어주고, 중복된 경우는 dp를 불러와 사용한다.

따라서 반복된 계산을 줄일 수 있다.

## 📒 코드

```python
def recur(x, y):    # 탑다운 DP
    if dp[x][y]:                    # 이미 계산했던 연산은 가져다가 사용한다.
        return dp[x][y]

    result = 1000                      # 비교할 최댓값
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:     # 최소값을 리턴
            result = min(result, arr[x][y] + recur(nx, ny))
    dp[x][y] = result          # 구한 값을 dp에 값을 넣어준다.
    return result


dx = [0, 1]     # 오른쪽, 아래
dy = [1, 0]
t = int(input())
for tc in range(1, 1 + t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]    # 반복된 연산을 줄이기 위한 DP
    dp[n - 1][n - 1] = arr[n - 1][n - 1]    # 기저 조건
    print(f'#{tc} {recur(0, 0)}')
```

## 🔍 결과

![image-20220329140542800](README.assets/image-20220329140542800.png)