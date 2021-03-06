# [Baekjoon] 1149. RGB๊ฑฐ๋ฆฌ [S1]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/1149

---

๋ฐฑํธ๋ํน์ผ๋ก ํ์ด๋ณด๋ฉด ์ฌ๊ท์ ๊น์ด๊ฐ ๋๋ฌด ๊น์ด์ ์๊ฐ์ด๊ณผ๊ฐ ๋๋ค. 

## ๐ ๋ฐฑํธ๋ํน - ์ฝ๋(์๊ฐ์ด๊ณผ)

```python
import sys
input = sys.stdin.readline


def recur(cur, total):
    global total_min
    if cur == n:
        if total < total_min:
            total_min = total
        return
    if total_min < total:
        return

    for i in range(3):
        if cur == 0 or i != visited[cur - 1]:
            visited[cur] = i
            recur(cur + 1, total + rgb[cur][i])
            visited[cur] = 0
            
            
n = int(input().rstrip())
rgb = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
total_min = 1000 * n
recur(0, 0)
print(total_min)            
```

---

๊ทธ๋์ stack์ ํ์ฉํ DFS๋ก ํ์ด๋ณธ๋ค. ์ฌ๊ท ์์ฐ๊ณ  dfs๋ก ํด๊ฒฐํด๋ณด๋ คํ๋๋ฐ ๋ง์ฐฌ๊ฐ์ง๋ก ์๊ฐ์ด๊ณผ๋ฅผ ํด๊ฒฐํ์ง ๋ชปํ๋ค.

## ๐ DFS ์ฝ๋(์๊ฐ ์ด๊ณผ)

```python
from collections import deque
import sys
input = sys.stdin.readline


def dfs(n):
    total_min = 1000 * n
    stack = deque()
    
    for i in range(3):
        stack.append((0, i, rgb[0][i]))

    while stack:
        v = stack.pop()
        if v[0] == n - 1:
            if v[2] < total_min:
                total_min = v[2]
            continue
        if total_min < v[2]:
            continue

        for i in range(3):
            if v[1] != i:
                stack.append((v[0] + 1, i, v[2] + rgb[v[0] + 1][i]))
    return total_min


n = int(input().rstrip())
rgb = [list(map(int, input().split())) for _ in range(n)]
print(dfs(n))
```

## ๐ ๊ฒฐ๊ณผ - ์๊ฐ ์ด๊ณผ

![image-20220314175532120](README.assets/image-20220314175532120.png)

---

๊ฒฐ๊ณผ๊ฐ์ ์ ์ฅํด๊ฐ๋ฉฐ ํด๊ฒฐํ๋ DP ๋ฐฉ๋ฒ์ผ๋ก ํ์ด๋ณด์๋ค.

rgb๊ฐ์ ๋ค ์ ์ฅํ ํ ๋ ๋ฒ์งธ ์ง๋ถํฐ ์ฒซ ๋ฒ์งธ ์ง์์ ์์ด ๋ค๋ฅธ ๊ฒ ์ค ์์ ์๋ฅผ ๋ํด์ฃผ๋ฉด์ ๋์๊ฐ๋ค.

์์  1๋ฒ์ ๊ทธ๋ฆผ์ผ๋ก ์ค๋ชํด๋ณธ๋ค.

- Input

  > 3
  > 26 40 83
  > 49 60 57
  > 13 89 99

![image-20220314202639115](README.assets/image-20220314202639115.png)

๊ฐ ์ง์ ํ์ฌ ์ง์ ์์ ๋ ๋๋ ๋น์ฉ์ ์ ๋๋ค.

2๋ฒ์งธ ์ค๋ถํฐ ์ด์ ์ ์ง ์ค ์ต์์ ๋น์ฉ์ผ๋ก ๊ตฌ๋งคํ  ์ ์๋ ๊ธ์ก์ ํ์ฌ ๋น์ฉ์ ๋ํด์ค๋ค.

![image-20220314202808973](README.assets/image-20220314202808973.png)

๋นจ๊ฐ ์ง์ ์ด์  ์ง ์ค ์ด๋ก, ํ๋์ผ ๋๋ง ๊ตฌ๋งคํ  ์ ์๋ค. ์ด๋ก์ด 40์ผ๋ก ๋ ์ ์ผ๋ 49 + 40์ 89์ด๋ค. ์ด๋ก๊ณผ ํ๋๋ ๋ค์๊ณผ ๊ฐ์ด ๊ตฌํด์ ์๋ฅผ ๋ฐ๊ฟ์ค๋ค.

์ ๊ฐ์ ๋ฐฉ๋ฒ์ ๊ณ์ ํด๋๊ฐ๋ค.

![image-20220314203003801](README.assets/image-20220314203003801.png)

๋ง์ง๋ง์ ๋จ์ ์ธ ๊ฐ์ ์ ์ค ์ต์๊ฐ์ ์ถ๋ ฅํ๋ค.

## ๐ DP ์ฝ๋

```python
import sys
input = sys.stdin.readline


n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):   # ์น ํ  ์ง๋ค
    for j in range(3):  # ๊ฐ ์์น ํ ์ง์ ์ต์ ๊ฐ
        min_rgb = 1000000
        for k in range(3):  # ์ด์ ์ ์น ํ๋ ์ง๋ค ํ์ธ
            if j != k:      # ์ด์ ์ ์ง๊ณผ ์์ด ๋ค๋ฅธ ๊ฒ๋ง ํ์ธ
                if min_rgb > rgb[i-1][k]:   # ์ต์๊ฐ ์ฐพ๊ธฐ
                    min_rgb = rgb[i-1][k]
        rgb[i][j] += min_rgb    # ์ต์๊ฐ์ ๋ํด์ค๋ค.

print(min(rgb[n-1]))
```

## ๐ DP ๊ฒฐ๊ณผ

![image-20220314175221698](README.assets/image-20220314175221698.png)

๋ฐฑํธ๋ํน์ด๋ DFS๋ฅผ ์ฌ์ฉํ๋ฉด ์๊ฐ์ด๊ณผ๊ฐ ๋ฐ์ํ๋์ง ํ์ธํ๋ ๋ฐฉ๋ฒ์ ๊ณต๋ถํด์ผ ํ๋ค..