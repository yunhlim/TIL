# [Baekjoon] 16236. ์๊ธฐ ์์ด [G3]

## ๐ ๋ฌธ์  : [์๊ธฐ ์์ด](https://www.acmicpc.net/problem/16236)

## ๐ ํ์ด

๊ตฌํ ๋ฌธ์ ์ด๋ค.

### ๋ฌธ์ ๋ฅผ ์์ฝ

- ๋ฌผ๊ณ ๊ธฐ M๋ง๋ฆฌ์ ์๊ธฐ ์์ด 1๋ง๋ฆฌ๊ฐ ์๋ค. 1์ด์ ์ํ์ข์ฐ๋ก ์ธ์ ํ ํ ์นธ์ฉ ์ด๋ํ๋ค.

- ์์ ์ ํฌ๊ธฐ๋ณด๋ค ํฐ ๋ฌผ๊ณ ๊ธฐ๊ฐ ์๋ ์นธ์ ์ง๋  ์ ์๊ณ , ๋๋จธ์ง ์นธ์ ๋ชจ๋ ์ง๋  ์ ์๋ค.

  - ์์ ์ ํฌ๊ธฐ๋ณด๋ค ์์ ๋ฌผ๊ณ ๊ธฐ๋ง ๋จน์ ์ ์๋ค.

  - ํฌ๊ธฐ๊ฐ ๊ฐ์ ๋ฌผ๊ณ ๊ธฐ๋ ๋จน์ ์ ์์ง๋ง, ์ง๋  ์๋ ์๋ค.

- ๊ฐ์ฅ ๊ฐ๊น์ด ๋ฌผ๊ณ ๊ธฐ๋ฅผ ๋จน์ผ๋ฌ ๊ฐ๋ค. 
  - ๊ฑฐ๋ฆฌ๊ฐ ๊ฐ๊น์ด ๋ฌผ๊ณ ๊ธฐ๊ฐ ๋ง๋ค๋ฉด ๊ฐ์ฅ ์์ ์๋ ๋ฌผ๊ณ ๊ธฐ, ๊ทธ๋ฆฌ๊ณ  ๊ฐ์ฅ ์ผ์ชฝ์ ์๋ ๋ฌผ๊ณ ๊ธฐ๋ฅผ ๋จน๋๋ค.

์์ ์ ํฌ๊ธฐ์ ๊ฐ์ ์์ ๋ฌผ๊ณ ๊ธฐ๋ฅผ ๋จน์ ๋๋ง๋ค ํฌ๊ธฐ๊ฐ 1 ์ฆ๊ฐํ๋ค. ์ฒ์ ์๊ธฐ ์์ด์ ํฌ๊ธฐ๋ 2์ด๋ค.

๋ ์ด์ ์์ง์ผ ์ ์์ผ๋ฉด ์ข๋ฃํ๋ค.



### ํ์ด ๋ฐฉ๋ฒ

์์ด์ ์์น์ ํฌ๊ธฐ๋ฅผ ๊ธฐ์ตํ๋ค.

BFS๋ก ํ์ํ๋ค. (๊ฐ์ฅ ๊ฐ๊น์ด ๋ฌผ๊ณ ๊ธฐ๋ฅผ ๋จน์ผ๋ฌ ๊ฐ๊ธฐ ์ํด)

์ฐํ์ข์ ๋ค ๋ฐฉํฅ ํ์

๊ฐ์ ๊ฑฐ๋ฆฌ์ ๋จน์ ์ ์๋ ๋ฌผ๊ณ ๊ธฐ๋ค์ ๋ฐฐ์ด์ ๋ด๋๋ค.

๋ฌผ๊ณ ๊ธฐ๋ค์ ๊ฐ์ฅ ์์ชฝ, ์ผ์ชฝ ์์ผ๋ก ์ค๋ฆ์ฐจ์ ์ ๋ ฌํ์ฌ ๋ฌผ๊ณ ๊ธฐ๋ฅผ ์ ํํ์ฌ ๋จน๋๋ค.

๋จน์ ์ ์๋ ๊ฒฝ์ฐ ์ข๋ฃํ๋ค.



## ๐ ์ฝ๋

```python
from collections import deque


def shark(x, y, move):            # ์๊ธฐ ์์ด๊ฐ ๋ค์ ๋จน์ด๋ฅผ ์ฐพ์ ์ด๋ํ๋ค.
    global eat, size
    que = deque()
    que.append([x, y])
    visited = [[0] * n for _ in range(n)]       # ๋ฐฉ๋ฌธํ๋์ง ํ์ธ
    visited[x][y] = 1
    dist = 0            # ๋ค์ ๋จน์ด๊น์ง์ ๊ฑฐ๋ฆฌ
    fishes = []         # ๊ฐ์ ๊ฑฐ๋ฆฌ์ธ ๊ฒฝ์ฐ ๋จน์ ์ ์๋ ๋ฌผ๊ณ ๊ธฐ์ ์ขํ๋ค
    while que:
        dist += 1
        for _ in range(len(que)):
            x, y = que.popleft()     # ์์ด์ ์์น
            for i in range(4):       # ๋ค ๋ฐฉํฅ์ผ๋ก ํ์
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < n and 0 <= ny < n):   # ๋ฒ์ ์์ ์๋์ง ํ์ธ
                    continue
                if visited[nx][ny]:               # ํ์ธํ๋ ์์น์ผ ๋
                    continue
                if 0 < arr[nx][ny] < size:      # ์์ ๋ฌผ๊ณ ๊ธฐ๊ฐ ์์ ๋
                    fishes.append([nx, ny])
                elif arr[nx][ny] == 0 or arr[nx][ny] == size:       # ํฌ๊ธฐ๊ฐ ๊ฐ์ ๋ฌผ๊ณ ๊ธฐ๊ฐ ์๊ฑฐ๋, ๋ฌผ๊ณ ๊ธฐ๊ฐ ์์ ๋
                    que.append([nx, ny])
                    visited[nx][ny] = 1
        if fishes:
            fishes.sort()               # ๋ฌผ๊ณ ๊ธฐ๋ค ์ค (๋งจ ์ => ๋งจ ์ผ์ชฝ)์ ์๋ ๋ฌผ๊ณ ๊ธฐ ์ ํ
            fish = fishes[0]
            eat += 1                    # ๋จน์ ํ์ + 1
            if eat == size:             # ๋ฌผ๊ณ ๊ธฐ๋ฅผ ๋จน์ ๊ฐ์๊ฐ ํฌ๊ธฐ๋ ๊ฐ์์ง๋ฉด ์งํ
                size += 1
                eat = 0
            arr[fish[0]][fish[1]] = 0             # ๋จน์ ๋ฌผ๊ณ ๊ธฐ๋ฅผ ์ ๊ฑฐ
            return shark(fish[0], fish[1], move + dist)
    return move


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
size = 2        # ์๊ธฐ ์์ด ์ด๊ธฐ ์ฌ์ด์ฆ : 2
eat = 0         # ๋จน์ ๋ฌผ๊ณ ๊ธฐ ์ซ์ 
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]       # ๋ค ๋ฐฉํฅ
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            print(shark(i, j, 0))
```

## ๐ ๊ฒฐ๊ณผ

![image-20220620153450920](README.assets/image-20220620153450920.png)