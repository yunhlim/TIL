# [Baekjoon] 14453. Hoof, Paper, Scissors (Silver) [S2]

## π λ¬Έμ 

https://www.acmicpc.net/problem/14453

---

Nμ΄ 100000μ΄λΌ O(n^2)μΌλ‘ ν΄κ²°νλ €κ³  νλ©΄ μκ°μ΄κ³Όκ° λλ€.

**λμ ν©**μ μ¬μ©νμ¬ O(n)μΌλ‘ ν΄κ²°νλ€.

Hκ° λ°μ, Pκ° λ³΄, Sκ° κ°μμ΄λ€.

H, P, Sμ λμ ν©μ μΈλ±μ€ λ³λ‘ κ°κ° 2μ°¨μ λ°°μ΄μ λ΄λλ€.

λμ ν©μ μ²«λ²μ§Έ μΈλ±μ€λΆν° νμνλ€. 

μ£Όλ¨Ή κ°μ λ³΄ μ€ 2κ°λ₯Ό λ½λλ€. μ€λ³΅ μλ μμ΄

> (H, P), (H, S), (P, H), (P, S), (S, H), (S, P)

Aμ Bλ₯Ό λ½μμΌλ©΄ Aμ`[0, i]` λμ ν©μ  Bμ`[i + 1 , n]` λμ ν©μ λνλ€.

λμ ν©μ κ΅¬νμΌλ Aλ νμΈν μΈλ±μ€ κ°μ λνλ©΄ λκ³  Bλ [-1]μΈ λ μΈλ±μ€μμ νμ¬ μΈλ±μ€λ₯Ό λΉΌμ€λ€.

λͺ¨λ  μΈλ±μ€μμ νμΈνλ©΄ O(n)μΌλ‘ νμν  μ μλ€.

## π μ½λ

```python
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + [input().rstrip() for _ in range(n)]
prefix = [[0, 0, 0] for _ in range(n + 1)]  # P, H, S

for i in range(1, n + 1):
    if arr[i] == 'P':
        prefix[i][0] += 1
    elif arr[i] == 'H':
        prefix[i][1] += 1
    else:
        prefix[i][2] += 1
    for j in range(3):
        prefix[i][j] += prefix[i - 1][j]

result = 0
for i in range(1, n + 1):
    for j in range(3):
        for k in range(3):
            if j != k:
                result = max(result, prefix[i][j] + prefix[-1][k] - prefix[i][k])
print(result)
```

## π κ²°κ³Ό

![image-20220322234754524](README.assets/image-20220322234754524.png)



