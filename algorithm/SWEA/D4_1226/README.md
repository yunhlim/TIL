# [SWEA] 1226. ๋ฏธ๋ก1 [D4]

## ๐ ๋ฌธ์ 

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD&categoryId=AV14vXUqAGMCFAYD&categoryType=CODE&problemTitle=%EB%AF%B8%EB%A1%9C1&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

๋ฏธ๋ก์ ์์์ ์ 2, ๋์ฐฉ์ ์ 3์ด๋ค.

๊ฐ ์ ์๋์ง ํ๋จํด์ผํ๋ **๋ธํ ํ์ + DFS ๋ฌธ์ **์ด๋ค.

ํ์ฌ ์์น๋ฅผ stack์ ๋ด๋๋ค.

stack์์ ํ๋์ฉ ๊บผ๋ด์ด ๋ค ๋ฐฉํฅ์ผ๋ก ํ์ธ ํ 3(๋์ฐฉ์ )์ด ์์ผ๋ฉด 1(๋์ฐฉ)์ ๋ฆฌํดํ๊ณ , ๊ธธ์ด ์์ผ๋ฉด ์คํ์ ๋ด๋๋ค.

์ง๋๊ฐ ๊ธธ์ ํ์ธํ์ง ์๊ธฐ ์ํด stack์์ ๊ฐ์ ๊บผ๋ด๋ฉด ์๋ ฅ์ ๋ฒฝ์ธ 1๋ก ๋ฐ๊พธ์ด์ค๋ค.

stack์ ๊ฐ์ด ์๋๋ฐ 3์ ๋๋ฌํ์ง ๋ชปํ์ผ๋ฉด 0(๋์ฐฉํ์ง ๋ชปํจ)์ ๋ฆฌํดํ๋ค.

## ๐ ๋ฌธ์ 

```python
def miro():     # ๋ฏธ๋ก ๊ฒฐ๊ณผ ๊ฐ๋ฅ ์ฌ๋ถ ํ๋ณ
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:  # ์์์  ํ์ธ
                s = (i, j)
    stack = [s]

    while stack:
        v = stack.pop()
        y, x = v[0], v[1]
        arr[y][x] = 1   # ๊ฐ์ง์น๊ธฐ๋ฅผ ์ํด ํ์ฌ ์์น๋ฅผ ๋ฒฝ์ผ๋ก ๋ง๋ ๋ค.
        for i in range(4):      # ๋ค ๋ฐฉํฅ์ผ๋ก ํ์ธ
            ny = y + dy[i]
            nx = x + dx[i]
            if arr[ny][nx] == 0:    # ๊ธธ์ธ์ง ํ์ธํ๊ณ  ๊ธธ์ด๋ฉด stack์ ๋ด๋๋ค.
                stack.append((ny, nx))
            elif arr[ny][nx] == 3:  # ๋์ฐฉ์ ์ ๋๋ฌํ๋์ง ํ์ธ
                return 1
    return 0        # ๋๋ฌํ์ง ์๋ ๊ฒฝ์ฐ


for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    dy = [0, 1, 0, -1]  # ์ฐ ํ ์ข ์
    dx = [1, 0, -1, 0]
    
    print(f'#{tc} {miro()}')
```

## ๐ ๊ฒฐ๊ณผ : Pass