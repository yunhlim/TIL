# [Programmers] Lv 3. 합승 택시 요금 [2021 KAKAO BLIND RECRUITMENT]

## 📚 문제 : [합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413)

## 📖 풀이

그림만 봐도 **다익스트라 알고리즘** 문제임을 알 수 있다.

그런데 단순 다익스트라 문제는 아니고, 두 사람이 S에서 함께 출발해서 중간 어느 지점에서 갈라진 후 A, B 각각에 도달했을 때 최소의 비용이 들 때를 찾는 문제이다.

여기서 중요한 포인트는 단방향이 아닌 **양방향(무방향) 그래프**라는 점이다.

경유하게 되는 특정 지점을 X라고 했을 때

S => X, X => A, X => B의 최소 값을 구하면 된다.

이 때 단방향 그래프인 경우는 S에서 모든 지점에 도달하게되는 값과 그 지점 각각에서 도달하는 모든 값들을 찾아야 한다. 즉, 지점의 개수가 100개이면 100번의 다익스트라를 구해 답을 구해야하는 것이다.

그렇지만 문제에서 양방향 그래프로 주어졌으므로, 우리는 X => A와 A => X가 같아진다.

따라서 S => X, A => X, B => X를 구하면 된다.

X에 여러 값이 들어와도 S, A, B에서 다익스트라만 3번 구하면 다 구할 수 있는 것이다.

다익스트라 알고리즘을 리뷰하면, 힙을 사용하면 된다. 힙에는 거리와 좌표 순으로 담아 거리가 작은 것부터 확인한다. 나머지는 큐를 동작하듯이 코드를 작성하면 된다.

## 📒 코드

```python
def solution(n, s, a, b, fares):
    import heapq

    INF = 100000 * 1000
    graph = [[] for _ in range(n + 1)]  # 연결관계 표시
    for x, y, d in fares:               # 양방향 그래프
        graph[x].append([d, y])
        graph[y].append([d, x])
    
    # 다익스트라
    def dykstra(x, dist_arr):   # x에서 모든 지점까지 가는 경우
        heap = [[0, x]]         # x값을 힙에 넣는다.
        dist_arr[x] = 0         # x는 자신의 노드로는 거리가 0
        
        while heap:              # 힙에 값이 없을 때까지 반복
            d, node = heapq.heappop(heap)
            if dist_arr[node] != d:     # 현재 힙에 있는 값이 최소로 업데이트된 값인지 확인
                continue
            
            for nxt_d, nxt_node in graph[node]:     # 연결된 노드들을 확인한다.
                if dist_arr[nxt_node] > d + nxt_d:      # 우회하는 경우가 더 적은 비용이면 변경
                    heapq.heappush(heap, [d + nxt_d, nxt_node])
                    dist_arr[nxt_node] = d + nxt_d


    dist_s = [INF for _ in range(n + 1)]    # s에서 모든 지점까지 비용
    dist_a = [INF for _ in range(n + 1)]    # a에서 모든 지점까지 비용
    dist_b = [INF for _ in range(n + 1)]    # b에서 모든 지점까지 비용
    dykstra(s, dist_s)
    dykstra(a, dist_a)
    dykstra(b, dist_b)

    min_cost = INF              # 최소 비용
    # s에서 i로 i에서 a, b로의 최소 비용의 합의 최소 값을 찾는다.
    # s=> i, i => a, i => b
    for i in range(1, n + 1):
        min_cost = min(min_cost, dist_s[i] + dist_a[i] + dist_b[i])
    
    return min_cost
```

