# [Baekjoon] 10828. μ€ν[S4]

## π λ¬Έμ 

https://www.acmicpc.net/problem/10828

---

>push X: μ μ Xλ₯Ό μ€νμ λ£λ μ°μ°μ΄λ€.
>
>pop: μ€νμμ κ°μ₯ μμ μλ μ μλ₯Ό λΉΌκ³ , κ·Έ μλ₯Ό μΆλ ₯νλ€. λ§μ½ μ€νμ λ€μ΄μλ μ μκ° μλ κ²½μ°μλ -1μ μΆλ ₯νλ€.
>
>size: μ€νμ λ€μ΄μλ μ μμ κ°μλ₯Ό μΆλ ₯νλ€.
>
>empty: μ€νμ΄ λΉμ΄μμΌλ©΄ 1, μλλ©΄ 0μ μΆλ ₯νλ€.
>
>top: μ€νμ κ°μ₯ μμ μλ μ μλ₯Ό μΆλ ₯νλ€. λ§μ½ μ€νμ λ€μ΄μλ μ μκ° μλ κ²½μ°μλ -1μ μΆλ ₯νλ€.

νλνλ μ‘°κ±΄λ¬ΈμΌλ‘ κ΅¬ννλ€. κ·Έλ°λ° μκ°μ΄κ³Όκ° λ°μνλ€..

## π μκ° μ΄κ³Ό μ½λ

```python
N = int(input())
stack = []

for i in range(N):
    command = input().split()
    if command[0] == 'push':
        stack += [int(command[1])]
    elif command[0] == 'pop':
        if len(stack):
            print(stack[-1])
            del stack[-1]
        else: print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack):
            print(0)
        else: print(1)
    else:
        if len(stack):
            print(stack[-1])
        else: print(-1)
```

## π μκ° μ΄κ³Ό κ²°κ³Ό

![image-20220201165725357](S4_10828.assets/image-20220201165725357.png)

---

inputμ΄ λλ €μ κ·Έλ°κ±°κ°μμ `sys.stdin.readline`μ μ¬μ©ν΄λ³Έλ€.

## π μ΅μ’ μ½λ

```python
import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    command = input().split()
    if command[0] == 'push':
        stack += [int(command[1])]
    elif command[0] == 'pop':
        if len(stack):
            print(stack[-1])
            del stack[-1]
        else: print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack):
            print(0)
        else: print(1)
    else:
        if len(stack):
            print(stack[-1])
        else: print(-1)
```

## π κ²°κ³Ό

![image-20220201165738541](S4_10828.assets/image-20220201165738541.png)

---

μλ ₯μ΄ λ§μ λ `import sys` `input = sys.stdin.readline`μ μ μ©νλ€.

μ λ κ² λ§¨ μμ μ¨μ£ΌκΈ°λ§ ν΄λ `input()`μ λκ°μ΄ μ¬μ©κ°λ₯νλ€.