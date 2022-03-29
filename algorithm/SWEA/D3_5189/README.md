# [SWEA] 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 [D3]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT

---

## 📖 풀이

중복되지 않는 순열 문제이다.

처음은 사무실에서 시작하고 각각의 관리구역을 돌게 재귀함수를 짠다.

관리구역을 겹쳐서 돌지 않게 visited로 방문표시를 한다.

마지막에는 무조건 사무실로 가니 사무실로 가는 값을 더해줘야 한다.

## 📒 코드

```python
def recur(cur, start, total):
    global min_total
    if cur == n - 1:    # 마지막에 사무실을 갈 때 사용량을 더한다.
        min_total = min(min_total, arr[start][0] + total)
        return
    for i in range(1, n):   # 사무실로 가면 안되니 1부터
        if visited[i] == 0 and start != i:
            visited[i] = 1
            recur(cur + 1, i, total + arr[start][i])
            visited[i] = 0


t = int(input())
for tc in range(1, 1 + t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]     # 방문 표시
    min_total = 1001
    recur(0, 0, 0)
    print(f'#{tc} {min_total}')
```

## 🔍 결과

![image-20220329141045561](README.assets/image-20220329141045561.png)