# [SWEA] 2001. ํ๋ฆฌ ํด์น [D2]

## ๐ ๋ฌธ์ 

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=2001&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

์ด์ค for๋ฌธ์ผ๋ก ํฉ์ ์ ๋ถ ํ์ธํ๋ฉฐ ๊ฐ์ฅ ํฐ ํฉ์ ์ถ๋ ฅํ๋ค.

## ๐ ์ฝ๋

```python
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)] # ํ๋ฆฌ๋ค์ด ๋ค์ด์๋ ๋ฆฌ์คํธ
    max_sum = 0
    for i in range(N-M+1):  # ํ์ํ  MxM์ ๋งจ ์ ์ธ๋ฑ์ค๋ฅผ ํํ๋ค.
        for j in range(N-M+1):
            sum_fly = 0
            for k in range(M):  # ๊ณ ๋ฅธ ์ธ๋ฑ์ค๋ฅผ ์ค์ฌ์ผ๋ก MxM์ ๋ค๋ชจ ์์ญ์ ํฉ์ ๊ตฌํ๋ค.
                for l in range(M):
                    sum_fly += flies[i+k][j+l]
            if max_sum < sum_fly:
                max_sum = sum_fly
    print(f'#{tc} {max_sum}')
```

## ๐ ๊ฒฐ๊ณผ : Pass