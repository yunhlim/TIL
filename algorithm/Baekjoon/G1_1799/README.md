# [Baekjoon] 1799. λΉμ [G1]

## π λ¬Έμ  : [λΉμ](https://www.acmicpc.net/problem/1799)

## π νμ΄

μ²΄μ€νμ ν¬κΈ°λ 10μ΄νμ μμ°μμ΄λ€. λ°λΌμ λ°±νΈλνΉμ μ΄μ©ν΄ ν΄κ²°ν΄μΌ νλ€.

μ‘°ν©μ νμ©ν μμ  νμμ μ΄μ©νλ©΄ 2μ 100μ κ³±λ§νΌμ κ²½μ°μ μκ° νμν΄ μκ°μ΄κ³Όκ° λ°μνλ€. λ°λΌμ λ°±νΈλνΉμ μ¬μ©νλ€.

- λ¨μ μΉΈμ λΉμμ λμ΄λ νμ¬ κ΅¬νλ μ΅λκ°λ³΄λ€ μκ±°λ κ°μΌλ©΄ κ°μ§μΉκΈ°νλ€.

μμ²λΌ νμ΄λ μκ°μ΄κ³Όκ° λ°μνλ€.



### Blackκ³Ό White μΉΈμ λλμ΄ μκ°!

μκ°μ΄κ³Όλ₯Ό ν΄κ²°νκΈ° μν΄μ μ²΄μ€νμ Black μΉΈκ³Ό White μΉΈμ λΆλ¦¬ν΄μ μκ°νλ€.

![image-20220618233103205](README.assets/image-20220618233103205.png)

μλλ©΄ λΉμμ Black μΉΈμ λ¬΄μ‘°κ±΄ BlackμΌλ‘λ§ μ΄λνκ³  Whiteλ λ¬΄μ‘°κ±΄ Whiteλ‘λ§ μ΄λνλ€.

λ°λΌμ λΆλ¦¬ν΄μ μκ°νλ€.



ν°μμΈ κ²½μ°μ κ²μ μΈ κ²½μ°λ‘ μκ°νλ €λ©΄ μ²΄μ€νμ μ΄λν  λ μ²΄μ€νμ ν¬κΈ°κ° μ§μμΈ κ²½μ°μ νμμΈ κ²½μ°λ‘ λΆλ¦¬νλ€.

- νμμΈ κ²½μ°

  ![image-20220618233720575](README.assets/image-20220618233720575.png)

  - 2μΉΈ μ© μ΄λνλ©΄ λλ€.

    

- μ§μμΈ κ²½μ°

  - μ§μμΈ κ²½μ°κ° μ€μνλ€.

  ![image-20220618233927344](README.assets/image-20220618233927344.png)

  - μ§μμΈ κ²½μ°λ 2μΉΈμ© μ΄λνλ©΄ μΈλ‘λ‘ κ°μ μμΉλ₯Ό λ³΄κ²λλ€.
  - 2μμλ 5λ‘ 7μμλ 8λ‘ μ΄λν΄μΌ νλ€. λ°λΌμ λ€μ μ€λ‘ μ΄λν  λ νμ¬ μΉΈμμ μ§μμ΄λ©΄ νμλ‘ νμμμΌλ©΄ μ§μλ‘ μ΄λνκ² μ€κ³νλ€.

νμ¬ μμΉμ λΉμμ λμμΌλ©΄ visited λ°°μ΄μ λΉμμ λμλ€κ³  νμνλ€.

λΉμμ΄ μλμ§ μ²΄ν¬ν  λλ λκ°μ  μμͺ½ λ°©ν₯λ§ μ²΄ν¬νλ€. μλνλ©΄ μΌμͺ½ μλΆν° μ€λ₯Έμͺ½ μλλ‘ λ΄λ €μ€λ, μλ λ°©ν₯μ μ΄μ°¨νΌ μμ§ λΉμμ λκΈ° μ μ΄λΌ μ²΄ν¬ν  νμκ° μλ€.

## π μ½λ

```python
def in_range(x, y):     # μ²΄μ€ν λ²μ μμΈμ§ νμΈ
    return 0 <= x < n and 0 <= y < n


def check(x, y):        # λκ°μ μ λΉμμλμ§ μ²΄ν¬
    for i in range(2):      # μΌμͺ½ μ, μ€λ₯Έμͺ½ μ λκ°μ  μ²΄ν¬
        nx = x + dx[i]
        ny = y + dy[i]
        while in_range(nx, ny):    # μ²΄μ€ν λ²μ μμΈ κ²½μ°
            if visited[nx][ny]:     # λκ°μ μ λΉμμ΄ λμ¬ μλ κ²½μ° False
                return False
            nx += dx[i]
            ny += dy[i]
    return True             # λκ°μ μ λΉμμ΄ μλ κ²½μ° True


def recur(x, y, cnt):   # 2μΉΈμ© κ±΄λλλ©° νμΈ
    color = (x + y) % 2     # νμ¬ μΉΈμ μ
    if not in_range(x, y):       # λ€ νμΈν κ²½μ°
        result[color] = max(result[color], cnt)      # μ΅λκ° κ°±μ 
        return
    if (n * n - 1 - (x * n + y)) // 2 + 1 + cnt <= result[color]:   # λ¨μ μΉΈμ λ€ λΉμμ λλ μ΅λκ°μ λ°κΎΈμ§ λͺ»νλ κ²½μ°
        return

    # λ€μ κ°μ μμ μ’ν κ° κ΅¬νκΈ°
    ny = y + 2
    nx = x + ny // n
    if ny >= n:      # λ€μ νμΌλ‘ μ΄λ
        if n % 2:       # μ²΄μ€νμ ν¬κΈ° nμ΄ νμμΈ κ²½μ°
            ny %= n
        else:           # μ²΄μ€νμ ν¬κΈ° nμ΄ μ§μμΈ κ²½μ°
            ny = 0 if ny % 2 else 1

    if arr[x][y] and check(x, y):   # λΉμμ λμ μ μμ λ
        visited[x][y] = 1
        recur(nx, ny, cnt + 1)
        visited[x][y] = 0
    recur(nx, ny, cnt)              # λΉμμ λμ§ μμ λ


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]       # λΉμμ λμ μ μλ μΉΈμ΄ μλ ₯μΌλ‘ μ£Όμ΄μ§λ€.

visited = [[0] * n for _ in range(n)]
dx, dy = [-1, -1], [-1, 1]  # μΌμͺ½ μ, μ€λ₯Έμͺ½ μ
result = [0, 0]     # μΉΈμ΄ ν°μμΈ κ²½μ°μ κ²μ μΈ κ²½μ° λλ μ κ΅¬νλ€.
recur(0, 0, 0)      # μΉΈμ΄ κ²μ μΈ κ²½μ°
recur(0, 1, 0)      # μΉΈμ΄ ν°μμΈ κ²½μ°
print(sum(result))      # μΉΈμ΄ ν°μ κ²μ μΈ κ²½μ°μ κ°μ λνλ€.
```

## π κ²°κ³Ό

![image-20220618234132046](README.assets/image-20220618234132046.png)