# [Baekjoon] 1927. ์ต์ ํ [S2]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/1927

---

ํ์ด์ฌ์ **ํ** ์๋ฃ๊ตฌ์กฐ ๋ฌธ์ 

๋ด์ฅ๋ **heapq**๋ฅผ ์ฌ์ฉํ๋ค.

์ต๋๊ฐ, ์ต์๊ฐ ์ฐ์ฐ์ ๋น ๋ฅด๊ฒ ํ๊ธฐ ์ํ ์์ ์ด์งํธ๋ฆฌ์ด๋ค.

heapq๋ **์ต์ ํ**์ผ๋ก ๊ตฌ์ฑ

>heapq.heappush(heap, item) : item์ heap์ ์ถ๊ฐ
>
>heapq.heappop(heap) : heap์ ์ต์๊ฐ์ pop, ์์ผ๋ฉด error
>
>heapq.heapify(list) : list๋ฅผ heap์ผ๋ก ๋ณํ

## ๐ ์ฝ๋

```python
import heapq, sys

n = int(input())
heap = []
for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
```

## ๐ ๊ฒฐ๊ณผ

![image-20220306003552209](README.assets/image-20220306003552209.png)