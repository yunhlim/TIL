# [Baekjoon] 14502. μ°κ΅¬μ [G5]

## π λ¬Έμ 

https://www.acmicpc.net/problem/14502

---

## π νμ΄

κ°λ‘ μΈλ‘κ° 8 x 8 μ΄λ―λ‘, λ²½μ 3κ° μΈμ°λ μ΅λ κ²½μ°μ μλ μ‘°ν©μΌλ‘ `64 * 63 * 62 / 3 * 2 * 1` μ΄λ€.

λ°λΌμ μ¬κ·ν¨μλ‘ λ²½μ μΈ κ°λ₯Ό μΈμ°λ λͺ¨λ  κ²½μ°λ₯Ό μ‘°ν©μΌλ‘ μ°Ύμμ€λ€. κ·Έλ¦¬κ³  λ²½μ μΈμμ€λ€.

λ²½μ μΈ κ° μΈμ΄ μκ°, κ°κ° BFSλ‘ λ°μ΄λ¬μ€λ₯Ό νμ° μν¨ ν, μμ  μμ­μ κ°μλ₯Ό μΌλ€.

## π μ½λ

```python
from collections import deque


def in_range(x, y):     # λ²μμ μνλμ§ νμΈ
    return 0 <= x < n and 0 <= y < m


def recur(cur, x, y):   # λ²½μ 3κ° μΈμμ€λ€.(μ‘°ν©)
    global max_safety
    if cur == 3:        # λ²½μ 3κ° λ€ μΈμ΄ κ²½μ°
        max_safety = max(bfs(), max_safety)     # bfs νμμ ν ν μ΅λκ° κ°±μ 
        return
    if y == m:          # yκ° μμ­μ λμ΄κ°λ©΄ λ€μ νμΌλ‘
        y = 0
        x += 1
    if x == n:          # xκ° μμ­μ λμ΄κ°λ©΄ μ’λ£
        return

    recur(cur, x, y + 1)        # λ²½μ μ μΈμ΄λ€.
    if arr[x][y] == 0:
        arr[x][y] = 1
        recur(cur + 1, x, y + 1)    # λ²½μ μΈμ΄λ€.
        arr[x][y] = 0


def bfs():          # bfsλ‘ μμ μμ­ νμ
    visited = [[0] * m for _ in range(n)]
    que = deque()
    cnt = 0     # λ°μ΄λ¬μ€μ λ²½μ μΌλ€.(μ¬μ§ν©μΌλ‘ μμ μμ­μ μΈκΈ° μν¨)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:      # λ°μ΄λ¬μ€λ₯Ό νμ λ΄λλ€.
                que.append((i, j))
                visited[i][j] = 1
                cnt += 1
            elif arr[i][j] == 1:    # λ²½λ λ°©λ¬Έ λΆκ°
                visited[i][j] = 1
                cnt += 1

    while que:          # λ°μ΄λ¬μ€ νμ°
        x, y = que.popleft()
        for nxt in range(4):
            nx = x + dx[nxt]
            ny = y + dy[nxt]
            # λ°°μ΄μ μμ­μ λμ΄κ°κ±°λ, μμ μμ­μ΄ μλ κ²½μ° continue
            if not in_range(nx, ny) or visited[nx][ny]:
                continue
            cnt += 1
            visited[nx][ny] = 1
            que.append((nx, ny))

    return n * m - cnt      # μμ μμ­μ ν¬κΈ°

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_safety = 0
recur(0, 0, 0)
print(max_safety)
```

## π κ²°κ³Ό

![image-20220402200941474](README.assets/image-20220402200941474.png)