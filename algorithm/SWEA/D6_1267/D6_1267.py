from collections import deque
import sys
sys.stdin = open("input.txt")
for tc in range(1, 11):
    V, E = map(int, input().split())
    # 정점(인덱스) => 정점들의 집합(set) , 정점(인덱스) <= 정점들의 집합(set)
    graph_lst = [[set() for _ in range(0, V+1)], [set() for _ in range(0, V+1)]] # 3차원으로 생성한다. 들어오는 경우, 나가는 경우
    in_lst = list(map(int,input().split())) # 입력
    queue = deque()         # BFS를 위해 queue 선언
    visited = []            # 탐색하여 순차적으로 담을 리스트
    for i in range(E):               
        graph_lst[0][in_lst[2*i]].add(in_lst[2*i+1]) # 정점 -> 정점 관계를 배열에 담아준다.
        graph_lst[1][in_lst[2*i+1]].add(in_lst[2*i]) # 정점 <- 정점 관계를 배열에 담아준다.
    for i in range(1, V+1): # 들어오는 간선이 없는 정점들만 택한다.
        if not graph_lst[1][i]:
            queue += [i]    # 찾은 정점들을 큐에 넣어준다.
    while queue:    # 큐에 값이 없으면 종료
        node = queue.popleft()  # 큐에서 하나씩 꺼내서 탐색한다.
        # 아직 한 번도 나오지 않았거나 들어오는 간선에 닿아있는 노드들이 다 출현한 경우
        if node not in visited and len(graph_lst[1][node]-set(visited)) == 0:   
            visited.append(node)    # 탐색한 걸 하나씩 담는다.
            queue += graph_lst[0][node] - set(visited) # 정점에서 연결된 정점들 중 아직 나오지 않는 정점들만 큐에 담는다.
    print(f'#{tc} ', end='')
    print(*visited)























# import sys
# sys.stdin = open("input.txt")
# T = 10
# for tc in range(1, 1+T):
#     V, E = map(int, input().split())

#     arr = [[0 for _ in range(V+1)] for _ in range(V+1)]   # padding을 더한 2차원 배열
#     visited = [0 for _ in range(V+1)]   # 등장한 간선인지 선택
#     result = []
#     in_lst = list(map(int,input().split()))
#     for i in range(E):               # 배열에 담아준다.
#         arr[in_lst[2*i]][in_lst[2*i+1]] = 1

#     for i in range(1, V+1):
#         for j in range(1, V+1):
#             if arr[j][i]:  # 방향선이 꽂히는 정점은 break
#                 break
#         else:
#             visited[i] = 1
#             result.append(i)
#             nows = [i]       
#             while nows != []:
#                 new_nows = []
#                 for now in nows:
#                     for k in range(1, V+1):
#                         if arr[now][k] and visited[k] == 0:   # 방향선을 받는 새로운 정점
#                             for l in range(1, V+1):
#                                 if arr[l][k] and visited[l] == 0:
#                                     break
#                             else:
#                                 visited[k] = 1
#                                 result.append(k)
#                                 new_nows.append(k)
#                 nows = new_nows[:]
#         if len(result) == V:
#             break
#     print(f'#{tc} ', end='')
#     print(*result)

            
