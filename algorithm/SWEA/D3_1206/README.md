# [SWEA] 1206. View [D3]

## ๐ ๋ฌธ์ 

๋งํฌ : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=1206&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

---

๋น๋ฉ์ ํ๋์ฉ ์ ํํ๋ฉด์ ์ ์์ผ๋ก -2, -1, 1, 2 ๋จ์ด์ง ๋น๋ฉ์ ์ต๊ณ  ๋์ด์ ๋น๊ตํด, ๋น๋ฉ์ด ์ต๊ณ  ๋์ด๋ณด๋ค ๋์ผ๋ฉด ๊ทธ ์ฐจ์ด๊ฐ ์กฐ๋ง๊ถ ์ธ๋ ์๊ฐ ๋๋ค. ๋ชจ๋  ๋น๋ฉ์ ์ ์ฉํ๋ค.

์ฝ๊ฒ ๋น๊ตํ๊ธฐ ์ํด -2,-1,1,2๋ฅผ list์ ๋ด์ ํ์ฉํ๋ค.

## ๐ ์ฝ๋

```python
import sys
sys.stdin = open('input.txt')   # input.txt ๋ถ๋ฌ์ค๋ ๋ฐฉ๋ฒ

T = 10  # ํ์คํธ ์ผ์ด์ค 10๊ฐ
location = [-2,-1,1,2]  # ๋น๋ฉ ์ ์์ผ๋ก 2์นธ ์ฉ ๋ณด๊ธฐ์ํด ๋ฆฌ์คํธ ์ง์ 

for tc in range(1, T+1):
    length = int(input())   # ๋ฆฌ์คํธ์ ๊ธธ์ด ์๋ ฅ
    arr = list(map(int, input().split()))
    jomang = 0  # ์กฐ๋ง๊ถ ์ธ๋ ์ ํฉ

    for i in range(2,length-2):
        top = 0 # ๋น๋ฉ ๊ฑฐ๋ฆฌ 2 ์ฌ์ด์์ ๊ฐ์ฅ ํฐ ๋น๋ฉ์ ๋์ด ์ฐพ๊ธฐ, ์ด๊ธฐํ
        for loc in location:
            if arr[i+loc] > top:
                top = arr[i+loc]    # ๊ฐ์ฅ ํฐ ๋น๋ฉ์ผ๋ก ์ ํ
        if arr[i] - top > 0: jomang += arr[i] - top # ์กฐ๋ง๊ถ ์ธ๋๋ฅผ ํฉ

    print(f'#{tc} {jomang}')    # ์ํ๋ ๋ชจ์์ผ๋ก ์ถ๋ ฅ
```

---

## ๐ ๊ฒฐ๊ณผ

![image-20220209173107690](D3_1206.assets/image-20220209173107690.png)