from collections import deque


for tc in range(1, 11):
    n, s = map(int, input().split())
    arr = [set() for _ in range(101)]   # 번호 : 1~100, 연결상태 표시, 중복된 값이 들어오니 set로 없애준다.
    visited = [0 for _ in range(101)]   # 연락 순서로 적어준다. 연락이 없으면 0

    temp = list(map(int, input().split()))
    for i in range(n // 2):     # 방향성이 있는 그래프
        arr[temp[i * 2]].add(temp[i * 2 + 1])
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:        # 연락이 끝날 때까지 시행
        v = queue.popleft()
        for v2 in arr[v]:
            if visited[v2] == 0:    # 연결된 정점들 중 아직 등장하지 않는 정점만 고른다.
                visited[v2] = visited[v] + 1    # 연락 순서를 +1 한다.
                queue.append(v2)        # 큐에 담아 다음 연락을 이어간다.
    v_max = 0
    for i in range(101):    # 연락순서가 가장 나중인 visited의 값이 큰 것 중 인덱스가 가장 큰 값을 고른다.
        if visited[i] >= visited[v_max]:
            v_max = i
    print(f'#{tc} {v_max}')