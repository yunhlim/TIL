## [Baekjoon] 9417. μ΅λ GCD [S4]

## π λ¬Έμ 

λ§ν¬ : https://www.acmicpc.net/problem/9417

---

μ£Όμ΄μ§ μλ ₯μμ μ‘°ν©μ μ΄μ©ν΄ 2κ°μ© κ³¨λΌμ€λ€.

μ΅λ κ³΅μ½μλ **μ ν΄λ¦¬λ νΈμ λ²**μ μ¬μ©νλ€.

## π μ½λ

```python
T = int(input())
for tc in range(T):
    num_lst = list(map(int, input().split()))
    max_gcd = 0 # κ΅¬ν κ°μ₯ ν° μ΅λ κ³΅μ½μ
    for i in range(len(num_lst)):    # μ€λ³΅λμ§ μλ λ μλ₯Ό κ³ λ₯΄κΈ° μν΄ μ€μ²© for λ¬Έμ μ¬μ©
        for j in range(i+1, len(num_lst)):
            if num_lst[i] >= num_lst[j]:  # λ μ μ€ aμ μμ μλ₯Ό λ΄λλ€.
                a, b = num_lst[j], num_lst[i]
            else:
                a, b = num_lst[i], num_lst[j]
            while b % a != 0:   # μ ν΄λ¦¬λ νΈμ λ²μ μ¬μ©ν΄ μ΅λ κ³΅μ½μλ₯Ό κ΅¬νλ€.
                a, b = b % a, a
            if max_gcd < a: # μ΅λ κ³΅μ½μκ° κ΅¬νλ κ°μ₯ ν° μ΅λ κ³΅μ½μλ³΄λ€ ν¬λ©΄ μλ°μ΄νΈ
                max_gcd = a
    print(max_gcd)
```

## π κ²°κ³Ό

![image-20220213125757565](README.assets/image-20220213125757565.png)

μ΅λ κ³΅μ½μ, μ΅μ κ³΅λ°°μλ μ ν΄λ¦¬λ νΈμ λ²μ νμ©ν΄ κ°λ¨νκ² ν΄κ²°νλ€.