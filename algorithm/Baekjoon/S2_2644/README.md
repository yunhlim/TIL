# [Baekjoon] 2644. μ΄μκ³μ° [S2]

## π λ¬Έμ  : [μ΄μκ³μ°](https://www.acmicpc.net/problem/2644)

## π νμ΄

μ΄μ κ³μ°μ λ μ μ  μ¬μ΄μ μ΅λ¨ κ±°λ¦¬λ₯Ό κ΅¬νλ©΄ λλ€.

λ°λΌμ BFSλ‘ ν΄κ²°νλ€.

μ£Όμ΄μ§ μ μ μ μ°κ²°μ κ·Έλνλ‘ μ°κ²°νλλ° μλ°©ν₯μΌλ‘ μ°κ²°νλ€.

μ£Όμ΄μ§ λ μ¬λμ λ²νΈ μ€ μ΄λ€ κ±Έλ‘ νμ λ΄μ μμνλ  μκ΄μλ€. νλλ‘ μμνλ©΄ λλ¨Έμ§ νλμ λμ°©νκ² νλ©΄ λλ€.

BFSμ depthλ₯Ό κ΅¬νλ κ±Έ νμ©ν΄μ ν΄κ²°νλ€.

## π μ½λ

```python
from collections import deque


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(m):  # μλ°©ν₯μΌλ‘ μ°κ²°
    x, y = map(int ,input().split())
    graph[x].append(y)
    graph[y].append(x)

que = deque()
que.append(a)
visited[a] = 1

d = 0
while que:      # BFS νμ
    sz = len(que)
    for _ in range(sz):
        v = que.popleft()
        if v == b:
            print(d)
            exit()
        for nxt in graph[v]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            que.append(nxt)
    d += 1

print(-1)
```

## π κ²°κ³Ό

![image-20220512224836982](README.assets/image-20220512224836982.png)