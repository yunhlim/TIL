# [Baekjoon] 2580. ์ค๋์ฟ  [G4]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/2580

---

๋ฐฑ์ค 2239. ์ค๋์ฟ  ๋ฌธ์ ๋ ๋๊ฐ๋ค. https://www.acmicpc.net/problem/2239

์ค๋ช์ **๋ฐฑ์ค 2239. ์ค๋์ฟ  ๋ธ๋ก๊ทธ ํฌ์คํ ๐** https://velog.io/@yunhlim/Baekjoon-2239.-%EC%8A%A4%EB%8F%84%EC%BF%A0-G4 ์ ์ฐธ๊ณ ํ๋ค. 

์๋ ฅ์ด๋ ์ถ๋ ฅ ํํ๋ง ๋ค๋ฅด๋ ๋ฐ๊ฟ์ ์ ์ถํ๋ค.

## ๐ ์ฝ๋

```python
def check(y, x, num):
    # ํ๊ณผ ์ด ์ฒดํฌ
    for k in range(9):
        if arr[y][k] == num or arr[k][x] == num:
            return False

    # 3x3 ์ฒดํฌ
    for i in range((y // 3) * 3, (y // 3) * 3 + 3):
        for j in range((x // 3) * 3, (x // 3) * 3 + 3):
            if arr[i][j] == num:
                return False
    return True     # ํ๋ ฌ, 3x3์ ๊ฐ์ ์ซ์๊ฐ ์์ผ๋ฉด ๋ฆฌํด True


def recur(y, x):
    while arr[y][x] != 0:
        if x == 8:      # x์ขํ๊ฐ ๋๊น์ง ๊ฐ๋์ง ํ์ธ
            if y == 8:  # (8, 8)์ ๋์ฐฉํ๋ฉด ์ถ๋ ฅํ๋ค.
                for i in range(9):
                    print(*arr[i])
                exit()  # ์ถ๋ ฅํ๊ณ  ์ข๋ฃ
            x = 0       # x์ขํ๋ฅผ 0์ผ๋ก ๊ฐ๊ณ  y์ขํ๋ฅผ ํ ์นธ ๋ด๋ฆฐ๋ค.
            y += 1
        else:
            x += 1      # ์๋๋ฉด x์ขํ๋ฅผ ํ ์นธ ์ ์ง

    for i in range(1, 10):  # 1 ~ 9๋ฅผ ์์ฐจ์ ์ผ๋ก ๋ฃ์ด์ค๋ค.
        if check(y, x, i):  # check ํจ์์์ true๊ฐ ๋์ฌ ๋๋ง
            arr[y][x] = i
            recur(y, x)
            arr[y][x] = 0

arr = [list(map(int, input().split())) for _ in range(9)]
recur(0, 0)
```

## ๐ ๊ฒฐ๊ณผ

![image-20220305174324260](README.assets/image-20220305174324260.png)