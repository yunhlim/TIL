# 벨만 포드 알고리즘
import sys
input = sys.stdin.readline


def bellman():      # 벨만포드 알고리즘, 음의 사이클이 있는지 확인
    for i in range(n):
        for j in range(1, n + 1):
            for node in graph[j]:
                if dist[node] > dist[j] + arr[j][node]:
                    dist[node] = dist[j] + arr[j][node]
                    if i == n - 1:      # n - 1번 이후인 n번에도 바뀌면 음의 사이클 존재
                        return 'YES'
    return 'NO'


for tc in range(int(input().rstrip())):
    n, m, w = map(int, input().split())     # n : 지점의 수 m : 도로의 수 w : 웜홀의 수
    INF = n * 10000
    arr = [[INF] * (n + 1) for _ in range(n + 1)]   # 거리를 담아준다.
    graph = [set() for _ in range(n + 1)]              # 관계를 담아준다.
    for i in range(m):  # 도로는 방향이 없는 그래프
        s, e, t = map(int, input().split())
        arr[s][e] = min(t, arr[s][e])       # 가장 작은 값을 넣어준다.
        arr[e][s] = min(t, arr[e][s])       # 가장 작은 값을 넣어준다.
        graph[s].add(e)
        graph[e].add(s)
    for i in range(w):  # 웜홀은 방향 있는 그래프
        s, e, t = map(int, input().split())
        arr[s][e] = min(-t, arr[s][e])      # 음수도 가장 작은 값을 넣어준다.
        graph[s].add(e)
    dist = [INF for _ in range(n + 1)]

    print(bellman())




# 플로이드 와샬 알고리즘(시간이 많이 걸린다)
# import sys
# input = sys.stdin.readline

# def floyd():
#     for k in range(1, n + 1):       # 거쳐갈 경유지
#         for i in range(1, n + 1):   # 출발지
#             if k == i:              # 경유지와 출발지는 달라야 한다
#                 continue
#             for j in range(1, n + 1):   # 목적지
#                 if k == j:          # 경유지와 목적지도 달라야 한다
#                     continue
#                 arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])   # 경유하는 거리가 짧으면 바꿔준다.
#                 if arr[i][i] < 0:           # 하나라도 0보다 작으면 YES를 출력
#                     return 'YES'                
#     return 'NO'

# for tc in range(int(input().rstrip())):
#     n, m, w = map(int, input().split())     # n : 지점의 수 m : 도로의 수 w : 웜홀의 수
#     INF = n * 10000
#     arr = [[INF] * (n + 1) for _ in range(n + 1)]
#     for i in range(m):  # 도로는 방향이 없는 그래프
#         s, e, t = map(int, input().split())
#         arr[s][e] = min(t, arr[s][e])       # 가장 작은 값을 넣어준다.
#         arr[e][s] = min(t, arr[e][s])       # 가장 작은 값을 넣어준다.
#     for i in range(w):  # 웜홀은 방향 있는 그래프
#         s, e, t = map(int, input().split())
#         arr[s][e] = min(-t, arr[s][e])      # 음수도 가장 작은 값을 넣어준다.
    
#     print(floyd())