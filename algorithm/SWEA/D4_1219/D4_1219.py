for _ in range(10):
    tc, N = map(int, input().split())   # 테스트케이스 개수, 길의 총 개수
    temp = list(map(int, input().split()))  # 입력받은 정점들의 관계
    arr = [[] for _ in range(100)]      # 0~99까지 인접 리스트
    
    for i in range(N):     # 입력받은 정점들의 관계를 인접 리스트에 담는다.
        arr[temp[2*i]].append(temp[2*i+1])  # 단방향

    visited = [0 for _ in range(100)]   # 방문한 정점 확인
    stack = [0]                         # 시작점은 0

    while stack and (not visited[99]):  # 원하는 경로에 도착하거나 더이상 진행할게 없으면 종료
        v = stack.pop()                 # stack에서 정점을 하나 뺀다.
        if not visited[v]:              # 방문하지 않은 정점일 때만 확인
            visited[v] = 1              # 방문시켜주고
            for i in arr[v]:            # 연결된 정점을 확인해 stack에 더해준다.
                if not visited[i]:      # 없으면 안 더해준다.
                    stack.append(i)

    if visited[99]:                     # 원하는 도착점에 도착했는지 확인
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')