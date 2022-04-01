# [SWEA] 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산 [D4]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYG3y62EcDFAVT&&

---

## 📖 풀이

최단거리를 구하는 문제이므로 **BFS**문제이다.

BFS로 다음 노드들로 깊어질 때마다 연산 횟수가 1 증가하니, size로 bfs를 탐색하기 전에 큐에 있는 개수를 세고, 매번 일정한 깊이의 노드들을 시행한 후 다음 노드들을 시행하기 전에 횟수들을 1 늘려준다. 그러면 깊이마다 탐색할 수 있다. 

값이 나오면 종료시키기 위해 함수에 작성한 후 return으로 종료한다. 

## 📒 코드

```python
from collections import deque


def in_range(x):        # 범위를 나타내는 함수
    return 0 < x <= 1000000


def bfs():
    visited = [0 for _ in range(1000001)]   # 연산의 중간과정은 항상 백만 이하의 자연수
    que = deque()
    que.append(n)
    d = 0       # 연산 횟수
    while que:
        size = len(que)
        for i in range(size):
            v = que.popleft()
            if v == m:
                return d

            for i in range(3):
                if not(in_range(v + cal[i])) or visited[v + cal[i]]:
                    continue
                visited[v + cal[i]] = 1
                que.append(v + cal[i])

            if in_range(v * 2) and visited[v * 2] == 0:     # 곱하기는 따로 작성한다.
                visited[v * 2] = 1
                que.append(v * 2)
        d += 1

t = int(input())
cal = [1, -1, -10]      # +, - 계산할 것들을 담아준다.
for tc in range(1, 1 + t):
    n, m = map(int, input().split())
    print(f'#{tc} {bfs()}')
```

## 🔍 결과

![image-20220401230629632](README.assets/image-20220401230629632.png)