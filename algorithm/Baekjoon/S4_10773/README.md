# [Baekjoon] 10773. μ λ‘ [S4]

## π λ¬Έμ  : [μ λ‘](https://www.acmicpc.net/problem/10773)

## π νμ΄

μ€νμ νμ©ν΄μ νΌλ€.

0μ΄ μλ μκ° λμ€λ©΄ μ€νμ μλ₯Ό λ΄κ³ , 0μ΄ λμ€λ©΄ μ€νμμ νλ κΊΌλΈλ€.

λ€ νμΈν ν μ€νμ μλ μλ€μ ν©μ μΆλ ₯νλ€.

## π μ½λ

```python
import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    x = int(input())
    if x:     # 0μ΄ μλ κ²½μ°
        stack.append(x)
    else:       # 0μΈ κ²½μ°
        stack.pop()

print(sum(stack))
```

## π κ²°κ³Ό

![image-20220728002835025](README.assets/image-20220728002835025.png)