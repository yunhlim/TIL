# [Baekjoon] 2239. ์ค๋์ฟ  [G4]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/2239

---

๋ฐฑํธ๋ํน ๋ฌธ์ ์ด๋ค.

![image-20220305151522362](README.assets/image-20220305151522362.png)

์ ์ฌ์ง์ฒ๋ผ ์ผ์ชฝ ์์์ ์์ํด 0์ด ์์ผ๋ฉด ๊ฐ์ 1~9๋ก ๋ฃ์ผ๋ฉด์ ์ฐพ์์ค๋ค. ๋ฐฑํธ๋ํน์ผ๋ก ์ฌ๊ทํจ์๋ฅผ ์ฌ์ฉํ๋ค. 

๊ฐ๋ก, ์ธ๋ก, 3x3 ๋ฐ์ค๋ฅผ ํ์ธํ๋ฉฐ ๋ฃ์ด์ค๋ค. ์ฒดํฌํ  ๋ ํจ์๋ฅผ ๋ฐ๋ก ์ฌ์ฉํ๋ค. ๊ฐ๋ก์ ์ธ๋ก์ ๊ฐ์ด ์๋์ง ํ์ธํด์ฃผ๊ณ , 3x3 ๋ฐ์ค์ ์๋์ง ํ์ธํ๊ธฐ์ํด ๋ฒ์๋ฅผ ์๋์ฒ๋ผ ๋ฃ์ด์ค๋ค.

- 3x3 ๋ฒ์ ์ฒดํฌ

>```python
>for i in range((y // 3) * 3, (y // 3) * 3 + 3):
>    for j in range((x // 3) * 3, (x // 3) * 3 + 3):
>```
>
>์ขํ ๊ฐ์ 3์ผ๋ก ๋๋ ๋ชซ์ 3์ ๊ณฑํ๋ฉด 0, 3, 6์ผ๋ก ๋จ์ด์ง๋ค.

๊ฐ์ ํ๋ ๋ฃ์ด์ฃผ๋ฉด ์ฌ๊ทํจ์์ ๋ค์ด๊ฐ ๋ค์ 0์ด ์๋ ๊ณณ์ ์ฐพ์ ๊ฐ์ ์ฒดํฌํด์ ๋ฃ์ด์ค๋ค. 

(8, 8)๊น์ง ๊ฐ๋ฉด ๊ฐ์ ์ถ๋ ฅํ๊ณ  `exit()`์ ์ฌ์ฉํ์ฌ ์ข๋ฃ์์ผ ์ค๋ค.

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
                    print(''.join(map(str, arr[i])))
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

arr = [list(map(int, input())) for _ in range(9)]
recur(0, 0)
```

## ๐ ๊ฒฐ๊ณผ

![image-20220305173901031](README.assets/image-20220305173901031.png)
