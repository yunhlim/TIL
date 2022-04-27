# [Baekjoon] 1504. 특정한 최단 경로 [G4]

## 📚 문제

https://www.acmicpc.net/problem/1504

---

## 📖 풀이

양수 가중치가 있는 최단경로를 구하는 문제이니 다익스트라 알고리즘을 활용한다.

경유해야하니 두 가지로 나눠서 생각한다.

>1 => v1 => v2 => n
>
>1 => v2 => v1 => n

6번 다익스트라를 사용한다고 생각할 수 있지만, 다익스트라 알고리즘은 출발지 기준 모든 경우를 구할 수 있다.

따라서 1이 출발점인 경우, v1, v2가 출발점인 경우 각각 구하면 되니까 3번만 다익스트라 알고리즘을 구한다.

>1에서 v1, v2 구하고
>
>v1 에서 v2, n 구하고
>
>v2 에서 v1, n 구한다.

두 가지 경우 다 최단 경로를 구할 수 없는 경우는 -1을 출력한다.

다익스트라 알고리즘을 구하기 위해서는 거리에 대한 배열을 INF로 초기화하는데 구할 수 없는 경우는, INF의 값을 출력하게 된다. 따라서 3가지 경로를 더한 값이 INF인 경우는 -1을 출력하면 된다.



## 📒 코드

```python
import heapq


def dijkstra(s, e1, e2):        # 다익스트라 s에서 출발, e1, e2 도착
    dist = [INF for _ in range(n + 1)]
    heap = [[0, s]]
    dist[s] = 0

    while heap:             # 다익스트라 알고리즘
        w, v = heapq.heappop(heap)      # 거리가 작은 값부터 꺼낸다. heap 사용
        if dist[v] != w:
            continue
        for w2, v2 in graph[v]:
            if dist[v2] > w + w2:       # 경유하는 경우가 더 작으면 갱신
                dist[v2] = w + w2
                heapq.heappush(heap, [w + w2, v2])

    return dist[e1], dist[e2]       # e1, e2까지의 최단 경로 리턴


INF = 100000000
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]      # 연결상태 표시
for i in range(e):
    n1, n2, w = map(int, input().split())
    graph[n1].append([w, n2])
    graph[n2].append([w, n1])       # 양방향 그래프

v1, v2 = map(int, input().split())  # 경유해야할 정점 v1, v2

one_to_v1, one_to_v2 = dijkstra(1, v1, v2)
v1_to_v2, v1_to_n = dijkstra(v1, v2, n)
v2_to_v1, v2_to_n = dijkstra(v2, v1, n)

path1 = one_to_v1 + v1_to_v2 + v2_to_n  # 1 => v1 => v2 => n
path2 = one_to_v2 + v2_to_v1 + v1_to_n  # 1 => v2 => v1 => n

result = min(path1, path2)
if result >= INF:       # 하나라도 연결되지 않는 것이 있으면 -1 리턴
    print(-1)
else:
    print(result)
```

## 🔍 결과

![image-20220427231751107](README.assets/image-20220427231751107.png)
