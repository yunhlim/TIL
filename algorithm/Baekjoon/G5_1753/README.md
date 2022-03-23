# [Baekjoon] 1753. 최단경로 [G5]

## 📚 문제

https://www.acmicpc.net/problem/1753

---

## 📖 풀이

플로이드 워셜 알고리즘을 공부하며 봤던 **다익스트라 알고리즘**이다.

하나의 정점에서 최단 경로를 구할 때 활용한다.

### 📌 다익스트라 알고리즘 참고 :

> https://m.blog.naver.com/ndb796/221234424646 

다익스트라 알고리즘의 핵심은 정점에서 연결되는 모든 정점을 확인할 것인데 가장 가까운 정점부터 확인한다.

가까운 정점을 들렸다가 다른 정점을 가는 경우가 더 빠르면 그 정점의 값을 바꾸어 준다. 바꾼 후 다시 가까운 정점을 확인해 바꿔주는 걸 반복한다.



배열의 크기가 큰데 인접행렬로 만들면 메모리 초과 발생한다! 

따라서 인접리스트로 만들어서 사용해야한다.



다익스트라 알고리즘은 정점을 확인할 때마다 최솟값이 바뀔 수 있어서 최솟값을 계속 확인해줘야 한다. 따라서 힙으로 구현하는 것이 매우 효율적이다.

힙에 노드의 최솟값을 넣어주면 힙에 같은 노드가 여러 개 쌓이는 경우가 생긴다. 따라서 정점과의 거리를 계속 변경했으니, 거리가 다르면 이전에 넣어놨던 정점이다. 따라서 꺼낸 후 continue로 힙에서 버리는 작업만 한다.

heap에 남은 노드가 없으면 종료한다.

## 📒 코드

```python
import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())        # 정점과 간선의 수
INF = n * 10                            # 나올 수 있는 가장 큰 값보다 크게 설정
arr = [[] for _ in range(n + 1)]
start = int(input().rstrip())           # 시작점
dp = [0 for _ in range(n + 1)]
for _ in range(e):                      # 가중치에 관한 그래프
    a, b, w = map(int, input().split())
    arr[a].append((w, b))               # 행 -> 열 일 때 값은 가중치

dp = [INF for _ in range(n + 1)]        # 시작점에서의 최단 거리
dp[start] = 0                           # 시작점은 0이다.

heap = []
heapq.heappush(heap, (0, start))        # 시작점을 담고 시작
while heap:
    w, v = heapq.heappop(heap)
    if dp[v] != w:                      # 변경된 값과 다르면 pass
        continue
    for t_w, t_v in arr[v]:
        if dp[t_v] > t_w + w:           # 최소값으로 넣어준다.
            dp[t_v] = t_w + w
            heapq.heappush(heap,(t_w + w, t_v))

for i in range(1, n + 1):
    print('INF' if dp[i] == INF else dp[i])
```

## 🔍 결과

![image-20220323195004729](README.assets/image-20220323195004729.png)
