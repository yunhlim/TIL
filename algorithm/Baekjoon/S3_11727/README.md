# [Baekjoon] 11727. 2xn νμΌλ§ 2 [S3]

## π λ¬Έμ  : [2xn νμΌλ§ 2](https://www.acmicpc.net/problem/11727)

## π νμ΄

DPλ‘ μκ°μ μ€μ¬ ν΄κ²°ν΄μΌνλ λ¬Έμ μ΄λ€.

μΈλ‘λ‘ νλ μΈμ μμ±νλ κ²½μ°μ κ°λ‘ 2κ°, 2x2 μ μ¬κ°ν νλλ‘ λ§λλ κ²½μ°μ μ 2κ°λ₯Ό νμ©ν΄μ ν΄κ²°νλ€.

μ νμμΌλ‘ λ³΄λ©΄, `dp[cur] = recur(cur - 2) * 2 + recur(cur - 1)` μ κ°μ΄ λμ¨λ€.

## π μ½λ

```python
def recur(cur):
    if cur == 1:
        return 1
    elif cur == 2:
        return 3

    if dp[cur]:
        return dp[cur]
    dp[cur] = recur(cur - 2) * 2 + recur(cur - 1)
    dp[cur] %= 10007
    return dp[cur]


n = int(input())
dp = [0 for _ in range(n + 5)]
print(recur(n))
```

##  π κ²°κ³Ό

![image-20220530225520323](README.assets/image-20220530225520323.png)