# [Baekjoon] 13305. ์ฃผ์ ์ [S4]

## ๐ ๋ฌธ์  : [์ฃผ์ ์](https://www.acmicpc.net/problem/13305)

## ๐ ํ์ด

์ต๋ ์ฃผ์  ๊ธ์ก์ ์๋ค.

ํ์ฌ ์ฃผ์ ์๊ฐ ์ง๊ธ๊น์ง ๋์จ ์ฃผ์ ์ ์ค ๋ฆฌํฐ ๋น ์ฃผ์ ๊ธ์ก์ด ์ต์์ด๋ฉด ๋ ์์ ์ฃผ์ ์๊ฐ ๋์ฌ ๋๊น์ง ์ฃผ์ ํ๋ฉด ๋๋ค.

์ฆ ์ต์ ๊ฐ์ ์ฐพ์ผ๋ฉฐ ๋์ฌ ๋๊น์ง ๊ฑฐ๋ฆฌ ๊ฐ์ ๊ณฑํด์ฃผ๋ฉด ๋๋ค.

์์ ๋ก ์ค๋ชํด๋ณธ๋ค.

- input

```
4
2 3 1
5 2 4 1
```

๋จผ์  ๋์์ ๊ฐ์๊ฐ ์ฃผ์ด์ง๋ค. ๋์์ ๊ฐ์๋ 4์ด๋ค.

๊ทธ๋ฆฌ๊ณ  ๊ฐ ๋์ ์ฌ์ด์ ๊ฑฐ๋ฆฌ๊ฐ ์์๋๋ก ์ฃผ์ด์ง๋ค.

๊ทธ ๋ค์ ์ค์๋ ์ฃผ์ ์์ ๋ฆฌํฐ ๋น ์ฃผ์ ๊ธ์ก์ด๋ค.

๊ทธ๋ฆผ์ผ๋ก ๊ทธ๋ฆฌ๋ฉด ๋ค์๊ณผ ๊ฐ์ด ๊ทธ๋ฆด ์ ์๋ค.

![image-20220725002947468](README.assets/image-20220725002947468.png)

ํ๋์์ด ํ์ฌ๊น์ง ๋์จ ์ต์ ๋ฆฌํฐ ๋น ์ฃผ์ ๊ธ์ก์ด๋ค.

๊ทธ๋ฌ๋ฉด 5์์ผ ๋ 2km๊ฐ๊ณ  2์์ผ๋ก 4km ๊ฐ๋๊น ์ด 18์์ ์ฐ๊ฒ ๋๋ค.

## ๐ ์ฝ๋

```python
n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = 1_000_000_000    # ํ์ฌ๊น์ง์ ์ต์ ๊ฐ์ ์ ์ฅํ๋ค.(์ด๊ธฐํ๋ ๋์ฌ ์ ์๋ ๊ฐ์ฅ ํฐ ์๋ก ์ด๊ธฐํ)

result = 0
for i in range(n - 1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    result += dist[i] * min_cost

print(result)
```



## ๐ ๊ฒฐ๊ณผ

![image-20220725003419560](README.assets/image-20220725003419560.png)