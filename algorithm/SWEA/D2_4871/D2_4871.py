T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [set() for _ in range(V+1)]       # 인접리스트를 set로 표현
    for i in range(E):
        s, e = map(int, input().split())    # 정점 -> 정점을 arr에 넣는다
        arr[s].add(e)
    visited = [0 for _ in range(V+1)]       # 나왔는지 확인
    s, e = map(int, input().split())        # 확인할 경로의 출발점과 도착점
    stack = [s]     # stack에 출발점을 넣는다.

    while stack and visited[e] == 0:        # stack이 없거나 원하는 도착점까지 도달했는지 확인
        v = stack.pop()
        if not visited[v]:                  # 방문하지 않는 정점만 확인
            visited[v] = 1                  # 방문했음을 표시
            for v2 in arr[v]:               # 정점에서 연결된 정점들을 순회
                if not visited[v2]:         # 방문하지 않은 정점을 방문
                    stack.append(v2)        # stack에 담는다.

    if visited[e]:                          # 원하는 정점에 방문했는지 체크
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')