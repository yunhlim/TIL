# [SWEA] 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용 [D3]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYGf7K180DFAVT

---

## 📖 풀이

**중복없는 순열** 문제이다. 1, 2, 3, ... 순서대로 A C B ... 처럼 중복되지 않게 고르면 된다.

그냥 재귀로 백트래킹 없이 해결하면 **O(n!)**의 시간복잡도로 n이 15까지 이니 15!이다.

1307674368000로 1조를 넘어가는 큰 경우의 수가 나오게 되니, **백트래킹**으로 줄여줘야 한다.

cur을 끝까지 돌며 현재까지 구한 최소 생산 비용보다 현재 구하고 있는 생산 비용이 더 크거나 같으면 절대 답이 될 수 없으므로 **가지치기** 해준다.

## 📒 코드

```python
def recur(cur, total):  # 중복 없는 순열
    global min_total
    if total > min_total:   # 가지치기
        return
    if cur == n:
        min_total = min(min_total, total)
        return
    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        recur(cur + 1, total + arr[cur][i])
        visited[i] = 0


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]     # 방문 표시
    min_total = 100 * n
    recur(0, 0)
    print(f'#{tc} {min_total}')
```

## 🔍 결과

![image-20220401103041819](README.assets/image-20220401103041819.png)