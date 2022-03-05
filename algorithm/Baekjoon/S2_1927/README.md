# [Baekjoon] 1927. 최소 힙 [S2]

## 📚 문제

https://www.acmicpc.net/problem/1927

---

파이썬의 **힙** 자료구조 문제

내장된 **heapq**를 사용한다.

최댓값, 최솟값 연산을 빠르게 하기 위한 완전이진트리이다.

heapq는 **최소 힙**으로 구성

>heapq.heappush(heap, item) : item을 heap에 추가
>
>heapq.heappop(heap) : heap의 최소값을 pop, 없으면 error
>
>heapq.heapify(list) : list를 heap으로 변환

## 📒 코드

```python
import heapq, sys

n = int(input())
heap = []
for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
```

## 🔍 결과

![image-20220306003552209](README.assets/image-20220306003552209.png)