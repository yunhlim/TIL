# [Baekjoon] 1753. ์ต๋จ๊ฒฝ๋ก [G5]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/1753

---

## ๐ ํ์ด

ํ๋ก์ด๋ ์์ ์๊ณ ๋ฆฌ์ฆ์ ๊ณต๋ถํ๋ฉฐ ๋ดค๋ **๋ค์ต์คํธ๋ผ ์๊ณ ๋ฆฌ์ฆ**์ด๋ค.

ํ๋์ ์ ์ ์์ ์ต๋จ ๊ฒฝ๋ก๋ฅผ ๊ตฌํ  ๋ ํ์ฉํ๋ค.

### ๐ ๋ค์ต์คํธ๋ผ ์๊ณ ๋ฆฌ์ฆ ์ฐธ๊ณ  :

> https://m.blog.naver.com/ndb796/221234424646 

๋ค์ต์คํธ๋ผ ์๊ณ ๋ฆฌ์ฆ์ ํต์ฌ์ ์ ์ ์์ ์ฐ๊ฒฐ๋๋ ๋ชจ๋  ์ ์ ์ ํ์ธํ  ๊ฒ์ธ๋ฐ ๊ฐ์ฅ ๊ฐ๊น์ด ์ ์ ๋ถํฐ ํ์ธํ๋ค.

๊ฐ๊น์ด ์ ์ ์ ๋ค๋ ธ๋ค๊ฐ ๋ค๋ฅธ ์ ์ ์ ๊ฐ๋ ๊ฒฝ์ฐ๊ฐ ๋ ๋น ๋ฅด๋ฉด ๊ทธ ์ ์ ์ ๊ฐ์ ๋ฐ๊พธ์ด ์ค๋ค. ๋ฐ๊พผ ํ ๋ค์ ๊ฐ๊น์ด ์ ์ ์ ํ์ธํด ๋ฐ๊ฟ์ฃผ๋ ๊ฑธ ๋ฐ๋ณตํ๋ค.



๋ฐฐ์ด์ ํฌ๊ธฐ๊ฐ ํฐ๋ฐ ์ธ์ ํ๋ ฌ๋ก ๋ง๋ค๋ฉด ๋ฉ๋ชจ๋ฆฌ ์ด๊ณผ ๋ฐ์ํ๋ค! 

๋ฐ๋ผ์ ์ธ์ ๋ฆฌ์คํธ๋ก ๋ง๋ค์ด์ ์ฌ์ฉํด์ผํ๋ค.



๋ค์ต์คํธ๋ผ ์๊ณ ๋ฆฌ์ฆ์ ์ ์ ์ ํ์ธํ  ๋๋ง๋ค ์ต์๊ฐ์ด ๋ฐ๋ ์ ์์ด์ ์ต์๊ฐ์ ๊ณ์ ํ์ธํด์ค์ผ ํ๋ค. ๋ฐ๋ผ์ ํ์ผ๋ก ๊ตฌํํ๋ ๊ฒ์ด ๋งค์ฐ ํจ์จ์ ์ด๋ค.

ํ์ ๋ธ๋์ ์ต์๊ฐ์ ๋ฃ์ด์ฃผ๋ฉด ํ์ ๊ฐ์ ๋ธ๋๊ฐ ์ฌ๋ฌ ๊ฐ ์์ด๋ ๊ฒฝ์ฐ๊ฐ ์๊ธด๋ค. ๋ฐ๋ผ์ ์ ์ ๊ณผ์ ๊ฑฐ๋ฆฌ๋ฅผ ๊ณ์ ๋ณ๊ฒฝํ์ผ๋, ๊ฑฐ๋ฆฌ๊ฐ ๋ค๋ฅด๋ฉด ์ด์ ์ ๋ฃ์ด๋จ๋ ์ ์ ์ด๋ค. ๋ฐ๋ผ์ ๊บผ๋ธ ํ continue๋ก ํ์์ ๋ฒ๋ฆฌ๋ ์์๋ง ํ๋ค.

heap์ ๋จ์ ๋ธ๋๊ฐ ์์ผ๋ฉด ์ข๋ฃํ๋ค.

## ๐ ์ฝ๋

```python
import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())        # ์ ์ ๊ณผ ๊ฐ์ ์ ์
INF = n * 10                            # ๋์ฌ ์ ์๋ ๊ฐ์ฅ ํฐ ๊ฐ๋ณด๋ค ํฌ๊ฒ ์ค์ 
arr = [[] for _ in range(n + 1)]
start = int(input().rstrip())           # ์์์ 
dp = [0 for _ in range(n + 1)]
for _ in range(e):                      # ๊ฐ์ค์น์ ๊ดํ ๊ทธ๋ํ
    a, b, w = map(int, input().split())
    arr[a].append((w, b))               # ํ -> ์ด ์ผ ๋ ๊ฐ์ ๊ฐ์ค์น

dp = [INF for _ in range(n + 1)]        # ์์์ ์์์ ์ต๋จ ๊ฑฐ๋ฆฌ
dp[start] = 0                           # ์์์ ์ 0์ด๋ค.

heap = []
heapq.heappush(heap, (0, start))        # ์์์ ์ ๋ด๊ณ  ์์
while heap:
    w, v = heapq.heappop(heap)
    if dp[v] != w:                      # ๋ณ๊ฒฝ๋ ๊ฐ๊ณผ ๋ค๋ฅด๋ฉด pass
        continue
    for t_w, t_v in arr[v]:
        if dp[t_v] > t_w + w:           # ์ต์๊ฐ์ผ๋ก ๋ฃ์ด์ค๋ค.
            dp[t_v] = t_w + w
            heapq.heappush(heap,(t_w + w, t_v))

for i in range(1, n + 1):
    print('INF' if dp[i] == INF else dp[i])
```

## ๐ ๊ฒฐ๊ณผ

![image-20220323195004729](README.assets/image-20220323195004729.png)
