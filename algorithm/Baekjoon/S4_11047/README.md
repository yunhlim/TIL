# [Baekjoon] 11047. λμ  0 [S4]

## π λ¬Έμ  : [λμ  0](https://www.acmicpc.net/problem/11047)

## π νμ΄

κ°μΉκ° μ¬λ¬ κ°μΈ λμ μ΄ λ¬΄νλλ‘ μ§κΈλλ€.

λμ λ€μ κ°μΉκ° μ£Όμ΄μ§λ©΄, μ΅μνμ λμ μ κ°μλ‘ μλ ₯μΌλ‘ μ£Όμ΄μ§ κ°μΉλ₯Ό λ§λλ λ¬Έμ μ΄λ€.

κ°μΉκ° ν° μ«μλΆν° λ£μ΄μ£Όλ©° νμΈνλ€. λμ μ΄ λ°°μλ‘ μ΄λ£¨μ΄μ Έ μμΌλ ν° μ«μλΆν° μ±μΈ μ μμΌλ©΄ μ±μ°λ©΄μ κ°λ©΄ λλ νΈνλ€.

λ΅μ΄ λμ¨ κ²½μ° λμ μ κ°μλ₯Ό μΆλ ₯νκ³  μ’λ£νλ€.

## π μ½λ

```python
def recur(cur, price, total_cnt):
    if not price:
        print(total_cnt)
        exit()
    
    cnt = price // arr[cur]
    if cnt:
        recur(cur - 1, price - cnt * arr[cur], total_cnt + cnt)
    else:
        recur(cur - 1, price, total_cnt)

n, k = map(int, input().split())
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())
recur(n - 1, k, 0)
```

## π κ²°κ³Ό

![image-20220717190148232](README.assets/image-20220717190148232.png)