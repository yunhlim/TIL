# [Baekjoon] 4963. μ¬μ κ°μ [S2]

## π λ¬Έμ 

https://www.acmicpc.net/problem/4963

---

## π νμ΄

μ°κ²° μμλ₯Ό κ΅¬νλ λ¬Έμ μ΄λ€.

λκ°μ μΌλ‘λ μ°κ²°ν  μ μμΌλ 8λ°©ν₯μ νμν΄μΌνλ€.

BFSλ‘λ ν  μ μλλ°, DFSλ‘ μ°κ²° μμμ κ°μλ₯Ό μ°Ύλλ€.

## π μ½λ

```python
def dfs(x, y):      # μ°κ²° μμ κ΅¬νκΈ°
    arr[x][y] = 0   # μ°κ²° μμλ λ€ 0μΌλ‘ λ°κΎΌλ€.

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny]:
            dfs(nx, ny)


dx = [0, 1, 1, 1, 0, -1, -1, -1]    # λκ°μ  λ°©ν₯λ κ΅¬νλ€.
dy = [1, 1, 0, -1, -1, -1, 0, 1]
while True:
    w, h = map(int, input().split())
    if w == 0:      # 0μ΄λ©΄ μ’λ£
        break
    arr = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                dfs(i, j)
                cnt += 1        # μ°κ²° μμμ κ°μ + 1
    print(cnt)
```

## π κ²°κ³Ό

![image-20220426233312573](README.assets/image-20220426233312573.png)