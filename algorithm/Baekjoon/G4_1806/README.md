# [Baekjoon] 1806. ๋ถ๋ถํฉ [G4]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/1806

---

## ๐ ํ์ด

์์ฐ์์ด๋ค. ์์์ธ ๊ฒฝ์ฐ๋ ๋์ ํฉ์ ํ์ฉํ๋ ๊ฑธ ์๊ฐํ  ์ ์๋๋ฐ ์์์ด๋ฏ๋ก **ํฌํฌ์ธํฐ**๋ก ํด๊ฒฐํ๋ค.

n๊ฐ์ ์์ด์์ ๋ถ๋ถํฉ์ด m์ด์์ผ ๋์ ์ต์ ๊ธธ์ด๋ฅผ ๊ตฌํ๋ ๋ฌธ์ ์ด๋ค.

๋ฌธ์ ์์๋ N, S์ธ๋ฐ ์์๋ก ๋ฐ๊ฟจ๋ค. ๐

ํฌํฌ์ธํฐ๋ก ํ์ด๋ณด๋ฉด, s, e๊ฐ ์์๋ถ๋ถ์์ ํจ๊ป ์ถ๋ฐํ๋ค.

e๊ฐ ์ธ๋ฑ์ค๋ฅผ ์ด๊ณผํ๋ ๊ฒฝ์ฐ ๋ฐ๋ณต๋ฌธ์ ์ข๋ฃํ๋ค.

๋งค๋ฒ ํ์ฌ total ๊ฐ์ m๊ณผ ๋น๊ตํด ๋ ํด ๋ ์ต์ ๊ธธ์ด๋ก ์๋ฐ์ดํธํ๋ค.

s์ e๊ฐ ๊ฐ์ ๊ฒฝ์ฐ๋ ๋ฌด์กฐ๊ฑด e๋ฅผ ํ ์นธ ์ ์งํ๋ค.

s๋ณด๋ค e๊ฐ ํฐ ๊ฒฝ์ฐ๋ 2๊ฐ์ง๋ก ์๊ฐํ๋ค.

total์ด m๋ณด๋ค ์์ ๊ฒฝ์ฐ๋ ์๋ฅผ ๋ ํค์์ผ ํ๋ e๋ฅผ ์ ์งํ๋ฉด์ total์์ ์ ์งํ ์์น์ ์๋ ๊ฐ์ ๋ํ๋ค.

total์ด m๋ณด๋ค ํฐ ๊ฒฝ์ฐ๋ ์๋ฅผ ๋ ์ค์ฌ์ผ ํ๋ s๋ฅผ ์ ์งํ๋ฉด์ total์์ s์ ์๋ ๊ฐ์ ๋บ๋ค.

## ๐ ์ฝ๋

```python
n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0]
INF = 100_000_001
min_len = INF

s, e = 0, 0
total = arr[e]
while e < n:
        if total >= m:
            min_len = min(min_len, e - s + 1)
        if total < m or s == e:
            e += 1
            total += arr[e]
        else:
            total -= arr[s]
            s += 1

print(0 if min_len == INF else min_len)
```

## ๐ ๊ฒฐ๊ณผ

![image-20220324012845897](README.assets/image-20220324012845897.png)