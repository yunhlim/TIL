# 위상 정렬
from collections import deque
import sys
input =  sys.stdin.readline

for tc in range(int(input().rstrip())):
    n, k = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    in_degree = [0 for _ in range(n + 1)]       # 들어오는 간선의 개수를 적어준다.
    graph = [[] for _ in range(n + 1)]  # 건설 순서의 반대를 넣어준다!!
    for _ in range(k):
        s, e = map(int, input().split())
        graph[s].append(e)
        in_degree[e] += 1
    w = int(input().rstrip())
    queue = deque()
    for i in range(1, len(in_degree)):      # 위상이 0인 것을 큐에 담아준다.
        if in_degree[i] == 0:
            queue.append(i)
    dp = arr[:]         # 간선에 들어오는 최대값으로 갱신해줄 값
    while queue:
        v = queue.popleft()
        if v == w:      # 원하는 w가 나오면 종료
            break
        for node in graph[v]:
            dp[node] = max(dp[node], arr[node] + dp[v])     # 최대값으로 갱신
            in_degree[node] -= 1
            if in_degree[node] == 0:    # 들어오는 간선을 다 처리해주면 큐에 넣는다.
                queue.append(node)
    print(dp[w])












# BFS 역추적으로 풀면 메모리초과, 시간초과
# from collections import deque
# import sys
# input = sys.stdin.readline

# for tc in range(int(input().rstrip())):
#     n, k = map(int, input().split())
#     arr = [0] + list(map(int, input().split()))
#     graph = [[] for _ in range(n + 1)]  # 건설 순서의 반대를 넣어준다!!
#     for _ in range(k):
#         s, e = map(int, input().split())
#         graph[e].append((s, arr[s]))
#     w = int(input().rstrip())
#     queue = deque()
#     queue.append((w, arr[w]))                 # 노드와 그 때 걸린 시간
#     time = arr[w]                             # 총 소요 시간
#     del arr
#     while queue:
#         v, t = queue.popleft()
#         for v2, t2 in graph[v]:
#             t2 = max(t + t2, t2)
#             time = max(time, t2)
#             queue.append((v2, t2))
#     print(time)