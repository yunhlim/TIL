# [Baekjoon] 11050. ์ดํญ ๊ณ์ 1[B1]

## ๐ ๋ฌธ์ 

https://www.acmicpc.net/problem/11050

---

**์ดํญ ๊ณ์**๋ฅผ ๊ตฌํ๋ ๋ฌธ์ ์ด๋ค. <sub>N</sub>C<sub>K</sub>์ธ๋ฐ N๊ณผ K๊ฐ 10๋ณด๋ค ์์ผ๋ ๊ทธ๋ฅ ๊ณฑํด์ ๋๋์ด์ ํผ๋ค.

N!/((N-K)!*K!)๋ฅผ ๊ณ์ฐํ๋ค.

๋จผ์  <sub>N</sub>C<sub>K</sub> = <sub>N</sub>C<sub>N-K</sub> ๋ฅผ ํ์ฉํด ๋ฐ๊พผ๋ค.

N๋ถํฐ N-K+1๊น์ง ์๋ฅผ ๊ณฑํด 1๋ถํฐ K๊น์ง ์๋ฅผ ๊ณฑํ ์์ ๋๋๋ค.

## ๐ ์ฝ๋

```python
N, K = map(int, input().split())

if N-K < K:
    K = N-K

up_nums = 1
down_nums = 1

for i in range(N,N-K,-1):
    up_nums *= i

for i in range(1,K+1):
    down_nums *= i

print(up_nums//down_nums)

```

## ๐ ๊ฒฐ๊ณผ

![image-20220201161841035](B1_11050.assets/image-20220201161841035.png)