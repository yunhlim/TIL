# [Baekjoon] 11723. ์งํฉ[S5]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/11723

---

**์งํฉ** ์๋ฃํ์ ํ์ฉํ ๋ฌธ์ ์ด๋ค.

**set()**๋ฅผ ์ฌ์ฉํด์ ๋ํ๋ธ๋ค.

์๋ ฅ์ด 3๋ฐฑ๋ง๊ฐ๊น์ง ์ฃผ์ด์ง ์ ์์ผ๋ ๊ผญ sys.stdin.readline()๋ฅผ ์ฌ์ฉํ๋ค.

์๋ ฅ์ tuple๋ก ๋ฐ๊ณ  ์๋ ฅ์ ๊ธธ์ด๊ฐ 2์ผ ๋๋ ๋ค์ ์ซ์๊ฐ ๋ถ์ ๊ฑธ๋ก ํ์ธํ๋ค.

์ซ์๋ ๊ผญ intํ์ผ๋ก ๋ณํํ์ฌ ๊ณ์ฐํ๋ค.

## ๐ ์ฝ๋

```python
import sys

n = int(input())
s1 = set()
for _ in range(n):
    x = tuple(sys.stdin.readline().split())
    if len(x) == 2:
        if x[0] == 'add':
            s1.add(int(x[1]))
        elif x[0] == 'remove':
            s1.discard(int(x[1]))
        elif x[0] == 'check':
            if int(x[1]) in s1:
                print(1)
            else:
                print(0)
        else:
            if int(x[1]) in s1:
                s1.discard(int(x[1]))
            else:
                s1.add(int(x[1]))
    else:
        if x[0] == 'all':
            s1 = set(range(1, 21))
        else:
            s1 = set()
```

## ๐ ๊ฒฐ๊ณผ

![image-20220306013233568](README.assets/image-20220306013233568.png)