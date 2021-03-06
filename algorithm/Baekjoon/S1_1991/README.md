# [Baekjoon] 1991. ํธ๋ฆฌ ์ํ [S1]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/1991

---

**์ด์ง ํธ๋ฆฌ ๋ฌธ์ **

๋ฌธ์๋ฅผ ord๋ฅผ ์ฌ์ฉํด ์ซ์๋ก ๋ฐ๊ฟ์ค๋ค.

A~Z๊น์ง ๋ค์ด์ฌ ์ ์์ผ๋ ์๋ ฅ์ ๋ฐ์ ๋ ๋๋คํจ์๋ฅผ ์ด์ฉํด ord('A')๋ฅผ ํด์ฃผ๊ณ  1๋ถํฐ ์์ํ๊ธฐ ์ํด 1์ ๋ํด์ค๋ค.

๊ทธ๋ฌ๋ฉด A~Z => 1~26์ผ๋ก ๋ฐ๋๋ค.

๋ฐฐ์ด์ 1~n์ด๋ n+1๋งํผ์ ๋ฐฐ์ด์ ๋ง๋ค๊ณ  ์ฐ๊ฒฐ๊ด๊ณ๋ฅผ ํ๋์ฉ ํ์ํด์ค๋ค.

>- **์ ์์ํ(VLR)** : ๋ถ๋ชจ๋ธ๋ ๋ฐฉ๋ฌธ ํ, ์์๋ธ๋๋ฅผ ์ข, ์ฐ ์์๋ก ๋ฐฉ๋ฌธ
>- **์ค์์ํ(LVR)** : ์ผ์ชฝ ์์๋ธ๋, ๋ถ๋ชจ๋ธ๋, ์ค๋ฅธ์ชฝ ์์๋ธ๋ ์์ผ๋ก ๋ฐฉ๋ฌธ
>- **ํ์์ํ(LRV)** : .์์๋ธ๋๋ฅผ ์ข์ฐ ์์๋ก ๋ฐฉ๋ฌธํ ํ, ๋ถ๋ชจ๋ธ๋๋ก ๋ฐฉ๋ฌธ

๋ค์์ ์ฌ๊ทํจ์๋ก ํ์ฉํด ํ์ด๋ณธ๋ค.

## ๐ ์ฝ๋

```python
def pre_order(v):	# ์ ์์ํ
    if v:
        return chr(v + ord('A') - 1) + pre_order(arr[v][0]) + pre_order(arr[v][1])
    else:
        return ''
        
        
def in_order(v):	# ์ค์์ํ
    if v:
        return in_order(arr[v][0]) + chr(v + ord('A') - 1) + in_order(arr[v][1])
    else:
        return ''
        
        
def post_order(v):	# ํ์์ํ
    if v:
        return post_order(arr[v][0]) + post_order(arr[v][1]) + chr(v + ord('A') - 1)
    else:
        return ''



n = int(input())
arr = [[0, 0] for _ in range(n + 1)]

for i in range(n):
    par, left, right = map(lambda x: ord(x) - ord('A') + 1 if x != '.' else 0, input().split())
    arr[par][0] = left
    arr[par][1] = right

print(pre_order(1))
print(in_order(1))
print(post_order(1))
```

## ๐ ๊ฒฐ๊ณผ

![image-20220316141422954](README.assets/image-20220316141422954.png)