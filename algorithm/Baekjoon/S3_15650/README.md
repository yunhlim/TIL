# [Baekjoon] N๊ณผ M (2) [S3]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/15650

---

## ๐ ํ์ด

์ค๋ฆ์ฐจ์์ผ๋ก ์ค๋ณต์๋ ์์ด์ด๋ ์กฐํฉ ๋ฌธ์ ์ด๋ค.

์ฌ๊ท๋ฅผ ํ์ฉํด ์ฝ๊ฒ ํด๊ฒฐํ๋ค.

๋ฐฐ์ด์ ๋ด์ ์ถ๋ ฅ์ํจ๋ค.

## ๐ ์ฝ๋

```python
def recur(cur, cnt):
    if cnt == m:
        print(*arr)
        return
    elif cur == n:
        return

    arr[cnt] = cur + 1
    recur(cur + 1, cnt + 1)   
    recur(cur + 1, cnt)
    

n, m = map(int, input().split())
arr = [0 for _ in range(m)]

recur(0, 0)
```

## ๐ ๊ฒฐ๊ณผ

![image-20220318171952204](README.assets/image-20220318171952204.png)