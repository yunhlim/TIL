# [Baekjoon] DFSμ BFS [S2]

## π λ¬Έμ  : [DFSμ BFS](https://www.acmicpc.net/problem/1260)

## π νμ΄

DFSμ BFS λ¬Έμ μ΄λ€.

λ μ μ  μ¬μ΄μ μ¬λ¬ κ°μ κ°μ μ΄ λμ¬ μ μλ κ·Έλν λ¬Έμ λ μ€λ³΅μ μ κ±°ν΄μ£ΌκΈ° μν΄ set μλ£νμ μ¬μ©νλ€.

μμ μμλλ‘ DFS, BFS νμμ ν΄μΌνλ set μλ£νμ μΈμ λ¦¬μ€νΈ ννλ‘ λ°κΏμ£Όλλ° μ€λ¦μ°¨μμΌλ‘ μ λ ¬νλ€.

DFSμ BFSλ₯Ό νμνλ©΄μ, κ²°κ³Όκ°μ λ°λ‘ λ¦¬μ€νΈμ μ μ₯ν΄μ£Όκ³  λ€ λκ³ λ ν μΆλ ₯νλ€.

## π μ½λ

```python
from collections import deque


def dfs(x):         # dfs νμ
    visited[x] = 1
    result.append(x)
    for nxt in graph[x]:
        if visited[nxt]:
            continue
        dfs(nxt)


n, m, v = map(int, input().split())
graph = [set() for _ in range(n + 1)]   # μΈμ λ¦¬μ€νΈλ‘ νννκΈ° μμ μ€λ³΅μ κ±°λ₯Ό μν΄ set() μ¬μ©

for i in range(m):
    a, b = map(int, input().split())    
    graph[a].add(b)                     # λ μ μ  μ¬μ΄μ μ¬λ¬ κ°μ κ°μ μ΄ λμ¬ μ μμΌλ μ€λ³΅ μ κ±°
    graph[b].add(a)

for i in range(n + 1):                  # μ«μκ° μμ μμΌλ‘ νμν΄μΌνλ λ¦¬μ€νΈλ‘ νλ³ν ν μ λ ¬
    graph[i] = sorted(list(graph[i]))

visited = [0 for _ in range(n + 1)]
result = []
dfs(v)
print(*result)

visited = [0 for _ in range(n + 1)]
que = deque()
que.append(v)
visited[v] = 1
result = [v]

while que:                  # bfs νμ
    node = que.popleft()
    for nxt in graph[node]:
        if visited[nxt]:
            continue
        visited[nxt] = 1
        result.append(nxt)
        que.append(nxt)

print(*result)
```

## π κ²°κ³Ό

![image-20220509134236443](README.assets/image-20220509134236443.png)