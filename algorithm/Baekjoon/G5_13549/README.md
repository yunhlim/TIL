# [Baekjoon] 13549. μ¨λ°κΌ­μ§ 3 [G5]

## π λ¬Έμ 

https://www.acmicpc.net/problem/13549

---

## π νμ΄

**BFS**λ‘ ν΄κ²°νλ€.

νμ¬ μμΉ κΈ°μ€ μκ°μ΄λν κ²½μ°λ λͺ¨λ κ°μ μκ°μΌλ‘ νμνλ€.

νμ μλΉμ΄μ μμΉμ κ·Έ λμ μκ°μ 0μΌλ‘ λ£μ΄μ€λ€.

λ°λΌμ λ¨Όμ  μμΉλ§λ€ μκ°μ λ΄μ λ°°μ΄μ λ§λ€μ΄μ£Όλλ° -1λ‘ μ΄κΈ°ν ν΄λλλ€.

νμΈν  κ°μ΄ 100000κΉμ§μ΄λ λμΆ© 200000κΉμ§ λ§λ€μ΄λλλ€. 

μκ°μ΄λμ ν μμΉ κΈ°μ€ x2λκΉ 200000λ³΄λ€ μ»€μ§λ κ°μ΄ λ€μ΄μ¬ μ μλ€.

μκ°μ΄ μ μ νμλ κ²½μ° νμ λ΄μμ€λ€.

λμμ μμΉμ μκ°μ λ΄μμ£Όλ©΄ κ·Έ λ κ°μ μΆλ ₯νκ³  μ’λ£νλ€.

## π μ½λ

```python
from collections import deque


def check(node):    # λμμ μμΉλ₯Ό μ°Ύμλμ§ νμΈ
    if node == k:
        print(visited[k])   # μκ°μ μΆλ ₯νκ³  μ’λ£
        exit()


def telpo(node):    # νλ ν¬νΈ
    nxt = node
    while nxt <= k:     # λμμ μμΉλ₯Ό λ°μ΄ λμ κ²½μ° 2λ°°λ₯Ό λ κ³±νμ§ μλλ€.
        nxt = nxt * 2               # x2 νλ ν¬νΈ
        if visited[nxt] != -1:      # λ°©λ¬Ένλ μ§μ μ΄λ©΄ μ’λ£(κ·Έ μ§μ  μ΄νλ μ΄λ―Έ λ€ λ°©λ¬Ένμ λμ΄μλ€.)
            break
        visited[nxt] = visited[node]    # λ°©λ¬Έ νμ
        check(nxt)                      # λμμ΄ μλμ§ νμΈ
        que.append(nxt)                 # νμ λ£λλ€.


n, k = map(int, input().split())
visited = [-1 for _ in range(200000)]   # λ°©λ¬Έν  λμ μκ°μ μ λλ€.
que = deque()
visited[n] = 0                          # μμμ μΈ μλΉμ΄μ μμΉμ μκ°μ 0μ λ£λλ€.
check(n)                                # μμμ μ κ°μ΄ μλμ§ νμΈ
que.append(n)                           # νμ λ£μ΄μ€λ€.
telpo(n)                                # νλ ν¬νΈ

while que:                              # νμ κ°μ΄ μμ λκΉμ§ λ°λ³΅
    v = que.popleft()                   # νμμ νλμ© κΊΌλΈλ€

    for i in [-1, 1]:                   # μμͺ½μΌλ‘ μ΄λ
        nxt = v + i
        if 0 <= nxt and visited[nxt] == -1:     # λ²μλ₯Ό λμ§ μμ λ, λ°©λ¬Ένμ§ μμ κ²½μ°
            visited[nxt] = visited[v] + 1
            check(nxt)
            que.append(nxt)
            telpo(nxt)
```

## π κ²°κ³Ό

![image-20220420145221887](README.assets/image-20220420145221887.png)