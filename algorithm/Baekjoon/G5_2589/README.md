# [Baekjoon] 2589. ๋ณด๋ฌผ์ฌ [G5]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/2589

---

## ๐ ํ์ด

**์ต๋จ ๊ฑฐ๋ฆฌ**๋ฅผ ๊ตฌํ๋ ๋ฌธ์ ๋ก **BFSํ์**์ ํ์ฉํ๋ค.

๋ชจ๋  ์ก์ง์ ์์น์์ BFS ํ์์ ํ๋ฉฐ,  BFS๋ก ์ด๋ ๊ฑฐ๋ฆฌ๊ฐ ๊ฐ์ฅ ๋จผ ๊ฑฐ๋ฆฌ๋ฅผ ์ถ๋ ฅํ๋ค.

size๋ก ๊ฐ์ ๊ฑฐ๋ฆฌ์ ์ ์ ๋ค์ ์ํํ๋ฉฐ ๋ค์ ๊ฑฐ๋ฆฌ์ ์ ์ ๋ค๊ณผ ๊ตฌ๋ณ์ ํด์ค๋ค.

์ํ๊ฐ ๋๋๋ฉด ๊ฑฐ๋ฆฌ๋ฅผ 1์ฉ ๋ํ๋ค. ๊ทธ๋ฆฌ๊ณ  ๋ค์ ๊ฑฐ๋ฆฌ์ ์ ์ ๋ค์ ๋ค์ ์ํํ๋ค.

## ๐ ์ฝ๋

```python
from collections import deque


def in_range(x, y):     # ๋ฒ์ ์์ ์ํ๋์ง ํ์ธํ  ํจ์
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    que = deque()
    que.append((x, y))
    visited[x][y] = 1
    d = -1
    while que:
        size = len(que)     # ๊ฐ์ ์ด๋๊ฑฐ๋ฆฌ์ ์ ์ ๋ค์ ๋ฌถ์ size
        for _ in range(size):       # ๊ฐ์ ์ด๋ ๊ฑฐ๋ฆฌ์ ์ ์ ๋ค์ ์ํ
            x, y = que.popleft()

            for nxt in range(4):    # ๋ค ๋ฐฉํฅ ํ์
                nx = x + dx[nxt]
                ny = y + dy[nxt]
                # ๋ฒ์๋ฅผ ์ด๊ณผํ๊ฑฐ๋, ๋ฐฉ๋ฌธํ๊ฑฐ๋, ๋ฐ๋ค์ธ ๊ฒฝ์ฐ๋ continue
                if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 'W':
                    continue
                visited[nx][ny] = 1
                que.append((nx, ny))
        d += 1  # ์ด๋ ๊ฑฐ๋ฆฌ
    return d


dx = [0, 1, 0, -1]  # ์ฐ ํ ์ข ์
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
arr = [input() for _ in range(n)]

max_d = 0       # ์ถ๋ ฅํ  ์ต๋ ๊ฑฐ๋ฆฌ ์ด๊ธฐํ
for i in range(n):                  # ๋ชจ๋  ์ก์ง์ ์์น์์ ์์  ํ์
    for j in range(m):
        if arr[i][j] == 'W':        # ๋ฐ๋ค์ธ ๊ฒฝ์ฐ continue
            continue
        max_d = max(max_d, bfs(i, j))   # ์ต๋ ๊ฑฐ๋ฆฌ๋ฅผ ๊ตฌํ๋ค.

print(max_d)
```

## ๐ ๊ฒฐ๊ณผ

![image-20220401235950459](README.assets/image-20220401235950459.png)