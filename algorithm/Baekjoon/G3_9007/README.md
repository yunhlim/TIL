# [Baekjoon] 9007. ์นด๋ ์ ์ [G3]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/9007

---

n ์ด 1000์ด๋ for๋ฌธ 2๊ฐ๊น์ง ์จ๋ ๋๋ค!

๋ฐฐ์ด์ 2๊ฐ์ฉ ๋ฌถ์ด๋ฒ๋ฆฐ๋ค.

1, 2๋ฐ์ ๋ชธ๋ฌด๊ฒ๋ฅผ ๊ฐ ํ ๋ช์ฉ ๋ํ ๋ฐฐ์ด์ ๋ง๋ค๊ณ  3, 4๋ฐ์ ๋ชธ๋ฌด๊ฒ๋ฅผ ๊ฐ ํ ๋ช์ฉ ๋ํ ๋ฐฐ์ด์ ๋ง๋ ๋ค.

์์์ ๋ง๋  ๋ ๋ฐฐ์ด์ ์ ๋ ฌ ์ํจ๋ค.

๊ทธ๋ฆฌ๊ณ  ๋ ๋ฐฐ์ด์ ํฌํฌ์ธํฐ๋ฅผ ํ์ฉํด ํด๊ฒฐํ๋ค.

## ๐ ์ฝ๋

```python
T = int(input())
for _ in range(T):
    k, n = map(int, input().split()) # k๋ ๋ณดํธ๊ฐ ์ํ๋ ๋ฌด๊ฒ, n์ ๊ฐ ๋ฐ๋น ์ธ์
    arr = [list(map(int, input().split())) for _ in range(4)] # 4 ๋ฐ์ ํ์๋ค์ ๋ชธ๋ฌด๊ฒ
    arr_1 = []
    arr_2 = []

    for i in range(n):
        for j in range(n):
            arr_1.append(arr[0][i] + arr[1][j])
            arr_2.append(arr[2][i] + arr[3][j])
    arr_1.sort()
    arr_2.sort()
    
    s = 0
    e = len(arr_1) - 1
    result = arr_1[s] + arr_2[e]
    while s < len(arr_1) and e >= 0:
        ssum = arr_1[s] + arr_2[e]
        if abs(k - result) > abs(k - ssum):
            result = ssum
        elif abs(k - result) == abs(k - ssum):
            result = min(ssum, result)
        
        if ssum < k:
            s += 1
        elif ssum > k:
            e -= 1
        else:
            break
    print(result)
```

## ๐ ๊ฒฐ๊ณผ

![image-20220222014141067](README.assets/image-20220222014141067.png)

python์ผ๋ก๋ ์๋๊ณ  pypy๋ก ํด์ผ ๊ฒจ์ฐ ๋์๊ฐ๋ค.. ๋ค๋ฅธ ์ฌ๋๋ค์ ์ฝ๋์ ์๊ฐ๋ ๋ณด๋ ๋น์ทํ๊ฒ ๋์จ๋ค.