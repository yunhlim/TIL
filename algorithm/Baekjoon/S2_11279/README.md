# [Baekjoon] 11279. 최대 힙 [S2]

## 📚 문제

https://www.acmicpc.net/problem/11279

---

heapq가 최소 힙으로 구현되어있기 때문에 **최대 힙** 구현을 위해서는 트릭이 필요하다.

-를 붙여 음수로 힙에 담는다. 반환할 때 -를 붙여 원래대로 바꾼 후 출력한다.

## 📒 코드

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

## 🔍 결과

![image-20220306004340433](README.assets/image-20220306004340433.png)