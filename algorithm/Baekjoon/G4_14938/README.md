# [Baekjoon] 14938. 서강그라운드 [G4]

## 📚 문제 : [서강그라운드](https://www.acmicpc.net/problem/14938)

## 📖 풀이

최단거리를 구하는 그래프 문제이다.

**다익스트라**를 이용해 해결하였다.

먼저 각 정점까지의 거리를 INF로 초기화하고, 초기 위치는 0으로 넣어준다.

INF는 탐색거리 + 1로 초기화한다. 이유는 나중에 INF가 아닌 정점들은 모두 탐색 가능하니 값을 구하기 더 편하다.

파이썬의 heapq 모듈을 활용해 heap을 활용해 다익스트라로 최단 거리를 구했다.

heap에는 거리와 정점을 함께 담기위해 리스트로 담아주었다.

초기 위치로부터 모든 정점까지의 최단 경로를 다 찾아주었으면, 이제 거리가 INF보다 작은 값들의 item 값들을 다 더해준다.

모든 정점에서 시행해주기 위해 n번 다익스트라를 시행한다.

최대값을 찾아 출력하면 끝이다.

## 📒 코드

```python
import heapq


def find_items(start):       # 현재 떨어진 위치에서 얻을 수 있는 아이템 최대 개수
    dijkstra(start)
    items_cnt = 0            # 찾을 수 있는 아이템의 수
    for i in range(1, n + 1):
        if min_d[i] != INF:
            items_cnt += items[i]
    return items_cnt


def dijkstra(start):        # 현재 위치 기준 각 정점까지의 최단 거리를 찾는다.
    min_d[start] = 0         # 현재 떨어진 위치는 거리가 0
    heap = []
    heapq.heappush(heap, [0, start])               # 현재 떨어진 위치와 거리 0을 큐에 저장
    while heap:
        d, v = heapq.heappop(heap)
        if min_d[v] != d:   # 지금 저장된 거리와 같은 경우만
            continue
        for nxt, l in graph[v]:
            if min_d[v] + l < min_d[nxt]:   # 거리가 더 작아지는 경우
                min_d[nxt] = min_d[v] + l
                heapq.heappush(heap, [min_d[nxt], nxt])   # 바뀐 값을 큐에 넣는다.


n, m, r = map(int, input().split())     # n: 지역의 개수, m: 수색 범위, r: 길의 개수
items = [0] + list(map(int, input().split())) # 각 지역의 아이템 수
graph = [[] for _ in range(n + 1)]      # 연결 관계 표시
INF = m + 1           # 수색 범위보다 큰 값을 설정
for i in range(r):
    a, b, l = map(int, input().split()) # a, b: 연결된 정점 번호, l: 길의 길이
    # 양방향 그래프
    graph[a].append([b, l])
    graph[b].append([a, l])

max_items = 0           # 가장 많이 얻을 수 있는 아이템의 개수를 찾는다.
for i in range(1, n + 1):   # 예은이는 1부터 n에 떨어질 수 있다.
    min_d = [INF for _ in range(n + 1)]       # 각 위치를 수색할 수 있는지 설정
    max_items = max(max_items, find_items(i))

print(max_items)       
```

## 🔍 결과

![image-20220612151813068](README.assets/image-20220612151813068.png)
