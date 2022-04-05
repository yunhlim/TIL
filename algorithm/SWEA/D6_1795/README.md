# [SWEA] 1795. 인수의 생일 파티 [D6]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4xuqCqBeUDFAUx

---

## 📖 풀이

X라는 정점을 출발점으로 하여 출발점부터 모든 정점까지의 최소 거리를 구하는 것과 X를 도착점으로 하여 모든 정점으로부터 X까지의 최소 거리를 구하는 문제를 풀어야 한다.



첫 번째 하나의 정점에서 모든 정점까지의 최소 거리는 다익스트라 알고리즘을 사용해야 함을 쉽게 알 수 있다.



**두 번째인 모든 정점에서 하나의 정점까지의 최소 거리를 구해야 하는데 이는 입력을 거꾸로 받아 해결할 수 있다.**

즉, 도착지점 -> 출발지점으로 입력을 받는 그래프를 하나 더 만들어서 다익스트라를 두 번 구해준다.



다익스트라를 2번 구현하니 코드를 재사용하기 위해 함수를 만들고, 입력으로는 그래프를 받는다.

정방향으로의 그래프와 역방향으로의 그래프를 따로 다익스트라 알고리즘으로 구해주고, 구한 두 dp 값을 더해줘 왕복 최소 시간을 구해준다.

그리고 그 때 가장 큰 값을 출력한다.

## 📒 코드

```python
import heapq


def dijkstra(graph):        # 다익스트라 알고리즘, 그래프 값을 입력으로
    dp = [INF for _ in range(n + 1)]
    heap = [[0, x]]     # 출발점을 담는다.
    dp[x] = 0           # 출발 위치는 0으로
    while heap:         # 힙구조를 활용한 다익스트라 구현
        t, v = heapq.heappop(heap)      # 힙에서 걸리는 시간이 작은 값을 꺼낸다.
        if dp[v] != t:      # 확인하지 않는 정점만, 이미 확인했으면 dp 값과 다르다.
            continue
        for t2, v2 in graph[v]:     # 연결된 정점들 순회
            if dp[v2] > t + t2:     # 최소값으로 바꿔줄 수 있으면 dp 값을 바꿔주고 힙에 넣어준다.
                dp[v2] = t + t2
                heapq.heappush(heap, [dp[v2], v2])
    return dp


t = int(input())
INF = 10000000000
for tc in range(1, 1 + t):
    n, m, x = map(int, input().split())
    forward = [[] for _ in range(n + 1)]
    reverse = [[] for _ in range(n + 1)]
    for i in range(m):
        s, e, t = map(int, input().split())
        forward[s].append([t, e])   # 가중치로 정렬하기 위해 가중치, 연결된 정점 순으로 넣는다.
        reverse[e].append([t, s])
    # x에서 출발하는 최단 경로
    f_dp = dijkstra(forward)
    # x에 도착하는 최단 경로
    r_dp = dijkstra(reverse)

    max_t = 0   # 왕복 최장 시간
    for i in range(1, n + 1):   # 출발시간과 도착시간의 합이 최대일 때
        max_t = max(f_dp[i] + r_dp[i], max_t)

    print(f'#{tc} {max_t}')
```

## 🔍 결과

![image-20220405163422505](README.assets/image-20220405163422505.png)