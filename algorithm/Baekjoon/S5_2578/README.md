# [Baekjoon] 2578. ๋น๊ณ  [S5]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/2578

---

5 X 5 ๋น๊ณ ํ์์ ๋น๊ณ  3์ค์ด ๋์ค๋ ์์๋ฅผ ์ถ๋ ฅํ๋ ๋ฌธ์ ์ด๋ค.

์  3๊ฐ๋ก ๊ฐ์ฅ ๋ง์ ์ ์ ์ด ๋์ค๋ ๊ฒฝ์ฐ๋ 3๊ฐ์ด๋ค. ๋ฐ๋ผ์ ๋ค์ ๊ทธ๋ฆผ๊ณผ ๊ฐ์ด

![image-20220225002921075](README.assets/image-20220225002921075.png)

๋น๊ณ ๊ฐ ์ธ์ค์ด ๋๋ ๊ฐ์ฅ ๋น ๋ฅธ ๊ฒฝ์ฐ๋ 12๋ฒ์ด๋ค.

๋ฐ๋ผ์ 12๋ฒ์ ์๋ ฅ์ ๋ฐ์ ๋น๊ณ ํ์ 0์ผ๋ก ํ์ํ๊ณ  ๋น๊ณ ๋ฅผ ํ์ธํ๋ค.

13๋ฒ์งธ๋ถํฐ๋ ์๋ ฅ๋ฐ์ ์ซ์๋ฅผ 0์ผ๋ก ๋ฃ์ด์ฃผ๊ณ  ๋น๊ณ ๋ฅผ ํ์ธํด์ค๋ค.

## ๐ ์ฝ๋

```python
def check(): # ๋น๊ณ  3๊ฐ ์ฒดํฌ
    bingo = 0
    cr1_cnt, cr2_cnt = 0, 0 
    for i in range(5):
        row_cnt, col_cnt = 0, 0
        if arr[i][i] == 0:      # ๋๊ฐ์  ์๋๋ก ๋ด๋ ค์ค๋ ๋ฐฉํฅ
            cr1_cnt += 1
        if arr[4-i][i] == 0:    # ๋๊ฐ์  ์๋ก ์ฌ๋ผ๊ฐ๋ ๋ฐฉํฅ
            cr2_cnt += 1
        for j in range(5): 
            if arr[i][j] == 0:  # ํ๋ฐฉํฅ
                row_cnt += 1
            if arr[j][i] == 0:  # ์ด๋ฐฉํฅ
                col_cnt += 1
        if row_cnt == 5:    # ํ, ์ด ๋ฐฉํฅ ํ์ธ
            bingo += 1
        if col_cnt == 5:
            bingo += 1
    if cr1_cnt == 5:    # ๋๊ฐ์  ํ์ธ
        bingo += 1
    if cr2_cnt == 5:
        bingo += 1

    if bingo >= 3:      # ๋น๊ณ  3์ค์ธ์ง ํ์ธ
        return True
    else:
        return False


arr = [list(map(int, input().split())) for _ in range(5)]
nums = []
for _ in range(5):
    nums += list(map(int, input().split()))

# 12๋ฒ์งธ๊น์ง 0 ๋ฃ์ด์ฃผ๊ธฐ
for i in range(5):
    for j in range(5):
        if arr[i][j] in nums[:12]:
            arr[i][j] = 0
cnt = 12
nums = nums[12:]    # 12๊ฐ ์์ ์ค๋ค.

if check():         # ๋น๊ณ  3์ค์ธ์ง ํ์ธ
    print(cnt)      # 12๋ฒ ์ถ๋ ฅ
else:               # ์ด์  ํ๋์ฉ ๋ฃ์ด๊ฐ๋ฉฐ ํ์ธ
    for v in nums:
        cnt += 1
        for i in range(5):  # ๋น๊ณ ํ์ 0์ ๋ฃ์ด์ค๋ค.
            for j in range(5):
                if arr[i][j] == v:
                    arr[i][j] = 0
        if check(): # ๋น๊ณ  3์ค์ด๋ฉด ํ์ ์ถ๋ ฅ
            print(cnt)
            break
```

## ๐ ๊ฒฐ๊ณผ

![image-20220225012608412](README.assets/image-20220225012608412.png)

๋น๊ณ  3๊ฐ ์ฒดํฌํ๋ ์ฝ๋๋ ๊ธธ์ง๋ง ์๋ฃ..