# [Baekjoon] 7806. GCD! [G4]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/7806

---

~~n๊ณผ k๊ฐ 10์ต์ด๋ ์ง์  ์ ํด๋ฆฌ๋ ํธ์ ๋ฒ์ผ๋ก ์ฐพ๋๊ฑด **์๊ฐ์ด๊ณผ**๊ฐ ๋ฐ์ํ๋ค.~~

๋ฐ๋ผ์ k๋ฅผ ์์ธ์๋ถํดํ์ฌ n!์ k์ ๋์ผํ ์์ธ์๊ฐ ๋ช ๋ฒ ๋์ค๋์ง ์ฐพ๋๋ค.

์์ธ์๋ถํด๋ฅผ ํ๋ ๋ฐฉ๋ฒ์ผ๋ก๋ **์ ๊ณฑ๊ทผ๋ณด๋ค ์๊ฑฐ๋ ๊ฐ์ ์์**๋ฅผ ์ฐพ๊ณ , ์์์ ๊ฐ์๋ฅผ ์ฐพ๋ ๋ฐฉ๋ฒ์ ๋ฐ๋ณตํ๋ฉฐ ์ฐพ์์ค๋ค. ์์์ ์์์ ๊ฐ์๋ฅผ ํจ๊ป ๋ด๊ธฐ ์ํด **๋์๋๋ฆฌ**๋ฅผ ํ์ฉํ๋ค.

**์์ธ์๋ถํด ์ ์ ๊ณฑ๊ทผ๋ณด๋ค ํฐ ์์ธ์๊ฐ ํ๋ ์กด์ฌํ  ๊ฐ๋ฅ์ฑ**์ด ์๋ค. ๊ทธ ๊ฐ๋ฅ์ฑ์ ํญ์ ์ฒดํฌํด์ฃผ๋ ๊ฒ์ด ํฌ์ธํธ์ด๋ค.

๋ง์ฝ k๋ฅผ ์์ธ์ ๋ถํด ํ์ ๋ `2^3 * 3^2`๊ฐ ๋์๋ค๋ฉด, n!์ 2๊ฐ ๋ช ๊ฐ์ธ์ง 3์ด ๋ช ๊ฐ์ธ์ง ํ์ํด ์ต๋ ๊ณต์ฝ์๋ฅผ ๊ตฌํ๋ค.

n!์ x์ ๊ฐ์๊ฐ ์กด์ฌํ์ง ํ์ํ๋ ๋ฐฉ๋ฒ์ n!//x๋ฅผ n!//x๊ฐ 0์ด ๋  ๋๊น์ง ๋ฐ๋ณตํ๋ฉฐ ๊ทธ ๊ฒฐ๊ณผ๊ฐ์ ๋ํ๋ฉด ๋๋ค.

์์ ์ผ์ด์ค๋ฅผ ์์์ ์๊ฐํ ๋ฐฉ์์ผ๋ก ํ์ด๋ณด์!

>4!๊ณผ 30์ด ์ฃผ์ด์ง๋ค.
>
>์ฐ์  30์ ์์ธ์๋ถํดํ๋ค. ๊ทธ๋ผ `2 * 3 * 5`์ด๋ค.
>
>4!์ 2๊ฐ ๋ช๊ฐ์๋์ง ํ์ธํ๊ธฐ์ํด 4!//2๋ฅผ ๊ณ์ ๋ฐ๋ณตํ๋ค.
>
>4!//2 = 12, 12//2 = 6, 6//2 = 3, 3//2 = 1 => ๋ค ๋ํ 22๊ฐ ์ด 2์ ๊ฐ์์ด๋ค.
>
>22๊ฐ์ 1๊ฐ ์ค ์ต์๊ฐ์ธ 1๊ฐ๊ฐ ์ต๋๊ณต์ฝ์์ ๊ณฑํด์ง 2์ ๊ฐ์์ด๋ค.
>
>์์ฒ๋ผ 3๊ณผ 5๋ ๋ฐ๋ณตํด์ ์ต๋๊ณต์ฝ์์ ๊ณฑํด์ง ๊ฐ์๋ฅผ ์ฐพ์์ค๋ค.

์๋ ฅ์ ๊ฐ์๊ฐ ์ ํด์ ธ ์์ง ์์ผ๋ฏ๋ก `try:  except: break`๋ฅผ ํ์ฉํด ์ข๋ฃ์์ผ์ค๋ค.

## ๐ ์ฝ๋

```python
while True:
    try:
        n, k = map(int, input().split())    # ์๋ ฅ์ ํ์ด ์๋ ๊ฒฝ์ฐ try except๋ก ํด๊ฒฐ
    except:
        break
    temp = k                    # k๋ฅผ ์์ธ์๋ถํด ๊ณ์ฐํ๊ธฐ ์ํด temp์ ๋ด๋๋ค. 
    smalls = {}                 # ์์ธ์์ ์์ธ์์ ๊ฐ์๋ฅผ ๋ด๊ธฐ ์ํด ๋์๋๋ฆฌ ์ฌ์ฉ
    for i in range(2, k+1):     # k์ ์์ธ์ ๋ถํด
        if i * i > k:           # ์ ๊ณฑ๊ทผ๋ณด๋ค ํด ๊ฒฝ์ฐ ์ข๋ฃ
            break
        while temp % i == 0:    # ์์ธ์์ผ ๊ฒฝ์ฐ ๊ฐ์๋งํผ ๋ด์์ค๋ค.
            temp //= i
            if smalls.get(i):
                smalls[i] += 1    # k์ ์์ธ์์ ๊ฐฏ์๋ฅผ ๋ด๊ธฐ ์ํด list๋ก ๋ด๋๋ค.
            else:
                smalls[i] = 1
    if temp != 1:               # ์ ๊ณฑ๊ทผ๋ณด๋ค ํฐ ์์ธ์ ์ถ๊ฐ
        smalls[temp] = 1         # k์ ์์ธ์๊ฐ ์์ง ๋ ๋์์ ๋ ์ถ๊ฐ

    result = 1
    for num, cnt in smalls.items():
        temp = n
        cnt2 = 0                # ์์ธ์๊ฐ n!์ ๊ณฑํด์ง ๊ฐ์
        while temp // num:
            temp //= num
            cnt2 += temp
            if cnt2 >= cnt:     # n!์ ์กด์ฌํ๋ ์์ธ์์ ๊ฐ์๊ฐ k์ ๊ฐ์๋ณด๋ค ํฌ๊ฑฐ๋ ๊ฐ์ผ๋ฉด ์ข๋ฃํ๋ค.
                break           # ๋ ํ์ํ  ํ์๊ฐ ์๋ค.

        result *= num ** min(cnt, cnt2) # n!์ ์กด์ฌํ๋ ์์ธ์์ ๊ฐ์์, k์ ์์ธ์ ๊ฐ์ ์ค ์ต์๊ฐ์ ์์ธ์์ ๊ฑฐ๋ญ์ ๊ณฑํด ๊ณฑํด์ค๋ค.
    print(result)
```

## ๐ ๊ฒฐ๊ณผ

![image-20220227020654858](README.assets/image-20220227020654858.png)