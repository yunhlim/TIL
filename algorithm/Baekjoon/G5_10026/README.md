# [Baekjoon] 10056. ์ ๋ก์์ฝ [G5]

## ๐ ๋ฌธ์  : [์ ๋ก์์ฝ](https://www.acmicpc.net/problem/10026)

## ๐ ํ์ด

๋ ๊ฐ์ง๋ก ๋๋์ด์ ์๊ฐํ๋ค.

1. ์ ๋ก์์ฝ์ด ์๋ ์ฌ๋
   - ๋นจ๊ฐ ์ด๋ก ํ๋์ผ๋ก ์ธ์ ๋ฆฌ์คํธ ๊ตฌํ๊ธฐ
2. ์ ๋ก์์ฝ์ธ ์ฌ๋
   - (๋นจ๊ฐ, ์ด๋ก์ ๊ฐ์ ๊ทธ๋ฃน), ํ๋์ผ๋ก ์ธ์ ๋ฆฌ์คํธ ๊ตฌํ๊ธฐ

๊ฒฐ๊ตญ ์ธ์ ๋ฆฌ์คํธ๋ฅผ ๊ตฌํ๋ ๋ฌธ์ ์ด๋ค.

์ขํ ๊ธฐ์ค ๋ค ๋ฐฉํฅ์ผ๋ก ํ์ํ๋ฉฐ ์ธ์ ๋ฆฌ์คํธ๋ฅผ ๊ตฌํด์ค๋ค.

์ ๋ก์์ฝ์ธ ๊ฒฝ์ฐ๋ ์๋ ฅ๋ฐ์ ๊ฐ์ด ํ๋์์ด๋ฉด ์ฐ๊ฒฐ๋ ๊ฐ์ด ๋ค ํ๋์์ด์ด์ผ ํ๊ณ , ํ๋์์ด ์๋๋ฉด ํ๋์์ด ์๋ ๊ฐ๋ค์ ์ฐ๊ฒฐ์์ผ์ฃผ๋ฉด ๋๋ค.

๋ ๋ฒ ์ํํด์ผํ๋ฏ๋ก visited๋ฅผ ์ด๊ธฐํ ํด์ฃผ๋ ๊ฒ์ ์ ์ํ์!

## ๐ ์ฝ๋

```python
import sys
sys.setrecursionlimit(10000)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y, color):       # ์ ๋ก์์ฝ์ด ์๋ ๊ฒฝ์ฐ ์ธ์ ๋ฆฌ์คํธ ๊ตฌํ๊ธฐ
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny) and not visited[nx][ny] and color == arr[nx][ny]:
            dfs(nx, ny, color)


def dfs_rg(x, y, color):    # ์ ๋ก์์ฝ์ธ ๊ฒฝ์ฐ ์ธ์ ๋ฆฌ์คํธ ๊ตฌํ๊ธฐ
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny) and not visited[nx][ny]:
            if color == 'B' and arr[nx][ny] == 'B':
                dfs_rg(nx, ny, color)
            elif color != 'B' and arr[nx][ny] != 'B':
                dfs_rg(nx, ny, color)


n = int(input())
arr = [input() for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# ์ ๋ก ์์ฝ์ด ์๋ ๊ฒฝ์ฐ
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        dfs(i, j, arr[i][j])
        cnt += 1

# ์ ๋ก ์์ฝ์ธ ๊ฒฝ์ฐ
visited = [[0] * n for _ in range(n)]
cnt_rg = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        dfs_rg(i, j, arr[i][j])
        cnt_rg += 1

print(cnt, cnt_rg)
```

## ๐ ๊ฒฐ๊ณผ

![image-20220522192928662](README.assets/image-20220522192928662.png)
