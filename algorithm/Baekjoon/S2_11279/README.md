# [Baekjoon] 11279. μ΅λ ν [S2]

## π λ¬Έμ 

https://www.acmicpc.net/problem/11279

---

heapqκ° μ΅μ νμΌλ‘ κ΅¬νλμ΄μκΈ° λλ¬Έμ **μ΅λ ν** κ΅¬νμ μν΄μλ νΈλ¦­μ΄ νμνλ€.

-λ₯Ό λΆμ¬ μμλ‘ νμ λ΄λλ€. λ°νν  λ -λ₯Ό λΆμ¬ μλλλ‘ λ°κΎΌ ν μΆλ ₯νλ€.

## π μ½λ

```python
import heapq, sys

n = int(input())
heap = []
for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x:
        heapq.heappush(heap, -x)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
```

## π κ²°κ³Ό

![image-20220306004340433](README.assets/image-20220306004340433.png)