# [Baekjoon] 9328. μ΄μ  [G1]

## π λ¬Έμ  : [μ΄μ ](https://www.acmicpc.net/problem/9328)

## π νμ΄

**κ΅¬ν** λ¬Έμ μ΄λ€.

**BFS**λ‘ νμνμ¬ ν΄κ²°νλ€.

λ¨Όμ  κ±΄λ¬Όμ νλλ¦¬ μ΄λλ  μμμ μ΄ λ  μ μλ€. λ°λΌμ νλλ¦¬ λͺ¨λ  μ μμ BFSλ₯Ό λλ €μ€λ€.

μ΄μ λ₯Ό λ°κ²¬νλ©΄ keys λ°°μ΄μ λ΄μμ€λ€.

λ¬Έμ λ°κ²¬νλ©΄ μ΄ μ μλ μ΄μ κ° μλμ§ νμΈνκ³  μ΄ μ μμΌλ©΄ μ΄μ΄μ νμνλ€.

λ¬Έμ μ΄ μ μμΌλ©΄ doors λ°°μ΄μ λ΄μμ€λ€.

νμνλ€κ° μ΄μ λ₯Ό λ§λλ©΄, μ΄μ λ₯Ό μΆκ°νλ€.

κ·Έλ¦¬κ³  μ΄ μ μλ λ¬Έμ μννλ©°, μλ‘ μΆκ°λ μ΄μ λ‘ μ΄ μ μλ λ¬Έμ΄ μλμ§ λ€μ ν λ² νμνλ€.

μ΄ μ μλ λ¬Έμ μλ‘μ΄ ν€λ‘λ μ΄ μ μμΌλ©΄ μ’λ£νλ€.

## π μ½λ

````python
from collections import deque


def open(door):        # μ΄ μ μλ keyκ° μλμ§ νμΈ
    if chr(ord(door) + 32) in keys:
        return True
    else:
        return False


def bfs(x, y):          # νμ¬ λΈλ μ£Όμλ₯Ό νμ
    que = deque()
    que.append([x, y])
    while que:
        x, y = que.popleft()
        for nxt in range(4):
            nx = x + dx[nxt]
            ny = y + dy[nxt]
            if 0 <= nx < h and 0 <= ny < w and go(nx, ny):
                que.append([nx, ny])


def go(x, y):       # κ° μ μμΌλ©΄ κ°κ³  True λ¦¬ν΄, μλλ©΄ μ κ°κ³  False λ¦¬ν΄
    global cnt
    if visited[x][y]:                   # μ΄λ―Έ λ°©λ¬ΈνμΌλ©΄ κ° μ μλ€.
        return False
    elif arr[x][y] == '.':                # λΉ κ³΅κ°μ λ§λλ©΄ κ° μ μλ€.
        visited[x][y] = 1
        return True
    elif arr[x][y] == '*':              # λ²½μ λ§λλ©΄ κ° μ μλ€.
        return False
    elif 'a' <= arr[x][y] <= 'z':       # μ΄μ λ₯Ό μ£Όμ μ λ
        keys.append(arr[x][y])          # μ΄μ  μΆκ°
        visited[x][y] = 1
        return True
    elif 'A' <= arr[x][y] <= 'Z':       # λ¬Έμ λ§μ£Όμ³€μ λ
        if open(arr[x][y]):             # μ΄ μ μλμ§ νμΈ
            visited[x][y] = 1
            return True
        else:
            doors.append([x, y])     # μ΄ μ μμΌλ©΄ μ΄μ§ λͺ»ν λ¬Έμ μΆκ°
            return False
    else:
        cnt += 1                        # λ¬Έμλ₯Ό λ§λ¬μ λ + 1
        visited[x][y] = 1               # λ°©λ¬Έ νμ
        return True


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n = int(input())
for _ in range(n):
    h, w = map(int, input().split())    # μ§λμ λμ΄ h, λλΉ w
    arr = [input() for _ in range(h)]   # μ§λ
    keys = list(input())                # μμ§νκ³  μλ ν€λ€
    doors = deque()      # μ΄μ§ λͺ»ν λ¬Έμ μ’νλ₯Ό νμ λ΄λλ€ : [x, y]
    visited = [[0] * w for _ in range(h)]   # λ°©λ¬Έ νμ
    cnt = 0     # νλν λ¬Έμμ μ

    # κ±΄λ¬Ό κ°μ₯μλ¦¬ νμ
    for i in range(h):
        if i == 0 or i == h - 1:    # μ²« νκ³Ό λ§μ§λ§ νμ μ λΆ λ€ νμ
            for j in range(w):
                if go(i, j):
                    bfs(i, j)
        else:                       # λλ¨Έμ§ νμ μ λλ§ νμ
            if go(i, 0):
                bfs(i, 0)
            if go(i, w - 1):
                bfs(i, w - 1)

    while doors:                    # μ΄μ§ λͺ»νλ λ¬Έλ€μ νμ
        change = 0
        sz = len(doors)
        for _ in range(sz):
            x, y = doors.popleft()
            if go(x, y):            # λ¬Έμ μ΄ μ μλμ§ νμΈνκ³  μ΄λ
                bfs(x, y)
                change = 1
            else:
                doors.append([x, y])
        if not change:              # λ μ΄μλ λ¬Έμ΄ μμ λλ§!
            break

    print(cnt)
````

## π κ²°κ³Ό

![image-20220628131403193](README.assets/image-20220628131403193.png)
