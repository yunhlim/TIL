# [Baekjoon] 16562. ์น๊ตฌ๋น [G3]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/16562

---

## ๐ ํ์ด

**์ฐ๊ฒฐ๋ฆฌ์คํธ** ๋ฌธ์ ์ด๋ค. ์ฐ๊ฒฐ๋ ๊ฒ๋ค ์ค ๊ฐ์ฅ ์์ ๊ฐ์ ๋ฆฌํดํด ๋ํด์ค๋ค.

๊ฐ์ฅ ์์ ๊ฐ๋ค์ ๋ค ๋ํ๋๋ฐ ๊ฐ์ง๊ณ  ์๋ ๋๋ณด๋ค ๋ง์ผ๋ฉด oh no๋ฅผ ์ถ๋ ฅํ๋ค.

DFS๋ฅผ stack์ผ๋ก ๋ง์ด ์ฌ์ฉํด์ ํด๊ฒฐํ๋๋ฐ ์ฌ๊ทํจ์๋ก ํ์ด๋ณธ๋ค.

์ฌ๊ท ๊น์ด์ ํ์ด ๊ฑธ๋ ค ๊น์ด ์ ํ์ ๋ฒ์๋ฅผ ๋ ๋ํ ํด๊ฒฐํ๋ค.

## ๐ ์ฝ๋

```python
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(cur):       # DFS ์ฌ๊ท ํจ์
    visited[cur] = 1
    fee = arr[cur]      # ์๊ธ์ ์ต์ ๊ฐ
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        fee = min(fee, dfs(nxt))
    return fee          # ์ต์ ์๊ธ ๋ฆฌํด


n, m, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
v = [[] * (n + 1) for _ in range(n + 1)]    # ์ธ์ ๋ฆฌ์คํธ์ ๊ด๊ณ๋ฅผ ๋ด๋๋ค.
for _ in range(m):                      # ๊ทธ๋ํ์ ๊ฐ์ ๋ฃ์ด์ค๋ค.
    a, b = map(int, input().split())
    v[a].append(b)                      # ์๋ก ์น๊ตฌ๋๊น ๋ฐฉํฅ์๋ ๊ทธ๋ํ
    v[b].append(a)
visited = [0 for _ in range(n + 1)]     # ๋ฐฉ๋ฌธ ํ์

total = 0
for i in range(1, n + 1):
    if visited[i] == 0:
        total += dfs(i)
        if total > k:
            print("Oh no")
            break
else:
    print(total)
```

## ๐ ๊ฒฐ๊ณผ

![image-20220330161950269](README.assets/image-20220330161950269.png)