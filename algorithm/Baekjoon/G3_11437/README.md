# [Baekjoon] 11437. LCA [G3]

## ๐ ๋ฌธ์  : [LCA](https://www.acmicpc.net/problem/11437)

---

## ๐ ํ์ด

๊ฐ์ฅ ๊ฐ๊น์ด ๊ณตํต ์กฐ์์ ๊ตฌํ๋ ๋ฌธ์ ์ด๋ค.

์ฌ๋ฌ๊ฐ์ง ๊ตฌ์์ผ๋ก ํด๊ฒฐํด๋ณด๋ ค๊ณ  ํ๋ค.

1. ๊ฐ ๋ธ๋๋ง๋ค ๋ถ๋ชจ๋ฅผ ์ ์ฅํ๋ค. ๋ ๋ธ๋์ ๋ถ๋ชจ๋ฅผ ํ์ธํด์ผํ  ๋ ๊ฐ ๋ธ๋์ ๋ถ๋ชจ๋ค์ ์์๋๋ก ๋ฆฌ์คํธ์ ์ ์ฅํ์ฌ ๋น๊ตํด์ฃผ์๋ค.

   ์ฌ๊ทํจ์๋ก ํธ์ถํ๋ ค๊ณ  ํ๋ ์๊ฐ์ด๊ณผ๊ฐ ๋ฐ์ํ๋ค.

2. ๊ฐ ๋ธ๋๋ง๋ค ๋ถ๋ชจ๋ค์ ๋ค ๋ฆฌ์คํธ์ ์์๋๋ก ์ ์ฅํ๋ฉด ๋ฉ๋ชจ๋ฆฌ์ด๊ณผ๊ฐ ๋ฐ์ํ๋ค.

3. 1๋ฒ ๋ฐฉ๋ฒ๋๋ก ๋ถ๋ชจ๋ฅผ ์ ์ฅํ ํ, ๊ฐ ๋ถ๋ชจ๋ค์ ๋ฐ๋ณต๋ฌธ์ผ๋ก ํธ์ถํ์ฌ ์ํํ๋ ์๊ฐ์ด ์ค๋ ๊ฑธ๋ ธ์ง๋ง ๊ฒจ์ฐ ๋์๊ฐ๋ค.

## ๐ ์ฝ๋(์๊ฐ์ด ๋ง์ด ๊ฑธ๋ฆฐ ์ฝ๋)

```python
from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
par = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

par[1] = 1  # ๋ฃจํธ
que = deque()
que.append(1)
while que:
    v = que.popleft()
    for node in graph[v]:
        if par[node]:
            continue
        par[node] = v
        que.append(node)

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    arr_a = [a]
    arr_b = [b]
    while True:
        arr_a.append(par[a])
        if par[a] == 1:
            break
        a = par[a]
    while True:
        arr_b.append(par[b])
        if par[b] == 1:
            break
        b = par[b]
    arr_a = arr_a[::-1]
    arr_b = arr_b[::-1]
    result = 0
    for i in range(min(len(arr_a), len(arr_b))):
        if arr_a[i] != arr_b[i]:
            break
        result = arr_a[i]
    print(result)
```

## ๐ ๊ฒฐ๊ณผ

![image-20220505203904929](README.assets/image-20220505203904929.png)

---

[๋๋๋น๋ ์ ํ๋ธ ์์ ์ฐธ๊ณ ](https://www.youtube.com/watch?v=O895NbxirM8)์ ๋ณด๊ณ  ์๊ฐ์ ์ค์ผ ๋ฐฉ๋ฒ์ ์๊ฐํด๋ณด์๋ค.

**depth**๊ฐ ํฌ์ธํธ์ด๋ค.

๊ฐ ๋ธ๋ ๋ณ๋ก depth๋ฅผ ๋ค ๊ตฌํ๋ค.

๋ ๋ธ๋์ ๊ณตํต ์กฐ์์ ๊ตฌํ  ๋, ๋ธ๋์ depth๋ฅผ ์์ ์ชฝ์ ๋ง์ถ๋ค. ์ด์ฐจํผ ํ๋์ depth๊ฐ 3์ด๊ณ  ๋ค๋ฅธ ํ๋๋ 5์ด๋ฉด depth๊ฐ 4, 5์ผ ๋์ ๊ฐ์ ๋ต์ด ๋  ์ ์๋ค. ๋ฐ๋ผ์ depth๊ฐ ์์ ์ชฝ์ ๋ง๊ฒ ํฐ depth์ธ ๋ธ๋๋ฅผ ๋ถ๋ชจ๋ก depth๊ฐ ๊ฐ์ ๋๊น์ง ๊ฑฐ์ฌ๋ฌ์ฌ๋ผ๊ฐ๋ค.

depth๊ฐ ๊ฐ์์ง๋ฉด ๊ทธ ๋๋ถํฐ ๋น๊ต๋ฅผ ํด๋๊ฐ๋ฉด์ ํ์ธํ๋ค.

## ๐ ์ฝ๋

```python
from collections import deque
import sys
input = sys.stdin.readline


def lca(a, b):
    while depth[a] != depth[b]:     # depth๊ฐ ๊ฐ์์ง๊ฒ
        if depth[a] > depth[b]:
            a = par[a]
        else:
            b = par[b]

    while a != b:       # ๊ณตํต ์กฐ์์ธ์ง ํ์ธ
        a = par[a]
        b = par[b]
    return(a)


n = int(input())
graph = [[] for _ in range(n + 1)]  # ๊ฐ ๋ธ๋์ ์ฐ๊ฒฐ ๊ด๊ณ

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)      # ์๋ฐฉํฅ ๊ทธ๋ํ

par = [0 for _ in range(n + 1)]     # ๊ฐ ๋ธ๋์ ๋ถ๋ชจ๋ฅผ ์ ์ฅ
depth = [0 for _ in range(n + 1)]   # ๊ฐ ๋ธ๋์ depth๋ฅผ ์ ์ฅ
par[1] = 1  # ๋ฃจํธ์ ๋ถ๋ชจ๋ธ๋๋ ์์ง๋ง ํ์ธ๋์์ ํ์!!
que = deque()
que.append(1)
while que:      # bfs
    v = que.popleft()
    for node in graph[v]:
        if par[node]:       # ์์ง ํ์ธ๋์ง ์๋ ๋ธ๋์ธ ๊ฒฝ์ฐ๋ง
            continue
        par[node] = v       # ๋ฃจํธ๋ถํฐ ๊ฐ ๋ธ๋์ ๋ถ๋ชจ ๋ธ๋๋ฅผ ์ ์ฅ
        depth[node] = depth[v] + 1      # ๊ฐ ๋ธ๋์ depth๋ฅผ ์ ์ฅ
        que.append(node)    # ๋ค์ depth๋ฅผ ํ์ธ

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
```

## ๐ ๊ฒฐ๊ณผ

![image-20220505210306760](README.assets/image-20220505210306760.png)
