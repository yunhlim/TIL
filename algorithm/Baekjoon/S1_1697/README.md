# [Baekjoon] 1697. μ¨λ°κΌ­μ§ [S1]

## π λ¬Έμ 

https://www.acmicpc.net/problem/1697

---

μ΅λ¨ μκ°μ μ°ΎμμΌ νλ€. λ°λΌμ **BFS νμ**μ νμ©νλ€. deque μλ£κ΅¬μ‘°λ₯Ό νμ©νλ€.

λμμ μμΉκ° 0λΆν° 100000κΉμ§ μ¬ μ μλ€. μλνλ©΄ -1, +1, *2λ₯Ό νμ©ν΄ μ΄λ€ μλ₯Ό λνλΌ λ κ·Έ μλ₯Ό λμ§ μκ³  μ΅λ¨ κ²½μ°μ μλ₯Ό μ°Ύμ μ μλ€. 

μ μ μ νμΈνλ©΄ κ·Έ μμ -1, +1 *2μ μ μ μ΄ νμ¬ λ°©λ¬Ένλμ§ νμΈνκ³  λ°©λ¬Ένμ§ μμμΌλ©΄ μ΄μ  μ μ μ λ΄κ²¨μλ κ°μ 1μ λνλ€.

λμμ΄ μλ μμΉκ° λμ€λ©΄ μΆλ ₯νλ€.

## π μ½λ

```python
from collections import deque


a, b = map(int, input().split())
visited = [-1 for _ in range(100001)]
queue = deque()
queue.append(a)
visited[a] = 0
while visited[b] == -1:
    v = queue.popleft()
    if v + 1 <= 100000 and visited[v + 1] == -1:
        visited[v + 1] = visited[v] + 1
        queue.append(v + 1)
    if v - 1 >= 0 and visited[v - 1] == -1:
        visited[v - 1] = visited[v] + 1
        queue.append(v - 1)
    if v * 2 <= 100000 and visited[v * 2] == -1:
        visited[v * 2] = visited[v] + 1
        queue.append(v * 2)

print(visited[b])
```

## π κ²°κ³Ό

![image-20220312143039254](README.assets/image-20220312143039254.png)