# [Baekjoon] 10866. λ±[S4]

## π λ¬Έμ 

https://www.acmicpc.net/problem/10866

---

>push_front X: μ μ Xλ₯Ό λ±μ μμ λ£λλ€.
>
>push_back X: μ μ Xλ₯Ό λ±μ λ€μ λ£λλ€.
>
>pop_front: λ±μ κ°μ₯ μμ μλ μλ₯Ό λΉΌκ³ , κ·Έ μλ₯Ό μΆλ ₯νλ€. λ§μ½, λ±μ λ€μ΄μλ μ μκ° μλ κ²½μ°μλ -1μ μΆλ ₯νλ€.
>
>pop_back: λ±μ κ°μ₯ λ€μ μλ μλ₯Ό λΉΌκ³ , κ·Έ μλ₯Ό μΆλ ₯νλ€. λ§μ½, λ±μ λ€μ΄μλ μ μκ° μλ κ²½μ°μλ -1μ μΆλ ₯νλ€.
>
>size: λ±μ λ€μ΄μλ μ μμ κ°μλ₯Ό μΆλ ₯νλ€.
>
>empty: λ±μ΄ λΉμ΄μμΌλ©΄ 1μ, μλλ©΄ 0μ μΆλ ₯νλ€.
>
>front: λ±μ κ°μ₯ μμ μλ μ μλ₯Ό μΆλ ₯νλ€. λ§μ½ λ±μ λ€μ΄μλ μ μκ° μλ κ²½μ°μλ -1μ μΆλ ₯νλ€.
>
>back: λ±μ κ°μ₯ λ€μ μλ μ μλ₯Ό μΆλ ₯νλ€. λ§μ½ λ±μ λ€μ΄μλ μ μκ° μλ κ²½μ°μλ -1μ μΆλ ₯νλ€.

μλ ₯μ΄ 10000κ°κΉμ§ λ€μ΄μ€λ `sys.stdin.readline`μ μ¬μ©νλ€.

μμ νμ΄λ³Έ μ€νκ³Ό ν μλ£κ΅¬μ‘°μ λ€λ₯΄κ² λ±(Deque)μ μμͺ½μΌλ‘ λ£κ³  μμͺ½μΌλ‘ λΊλ€.

## π μ½λ

```python
import sys
input = sys.stdin.readline

N = int(input())
deque = []

for _ in range(N):
    command = input().split()
    
    if command[0] == 'push_front':
        deque = [command[1]] + deque
    elif command[0] == 'push_back':
        deque = deque + [command[1]]
    elif command[0] == 'pop_front':
        if len(deque):
            print(deque[0])
            del deque[0]
        else: print(-1)
    elif command[0] == 'pop_back':
        if len(deque):
            print(deque[-1])
            del deque[-1]
        else: print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if len(deque):
            print(0)
        else: print(1)
    elif command[0] == 'front':
        if len(deque):
            print(deque[0])
        else: print(-1)
    else:
        if len(deque):
            print(deque[-1])
        else: print(-1)
```

## π κ²°κ³Ό

![image-20220201234335943](S4_10866.assets/image-20220201234335943.png)

