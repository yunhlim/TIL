from collections import deque

t = int(input())
for tc in range(1, t + 1):
    e, par = map(int, input().split())    # e: 간선의 개수, par: 확인할 서브 트리의 루트 노드
    temp = list(map(int, input().split()))  # 입력받은 부모 자식 노드 쌍
    arr = [[0, 0] for _ in range(e + 2)]    # 부모 자식 관계

    for i in range(e):  # 부모와 자식 노드 관계를 arr 배열에 담는다.
        p, c = temp[i * 2], temp[i * 2 + 1]
        if arr[p][0] == 0:
            arr[p][0] = c
        else:
            arr[p][1] = c

    queue = deque()
    queue.append(par)
    cnt = 0

    while queue:    # BFS로 탐색하며 개수를 센다.
        v = queue.popleft()
        cnt += 1    # 연결된 노드들의 개수 + 1
        for i in range(2):  # 연결됐는지 확인
            if arr[v][i] == 0:
                break
            queue.append(arr[v][i])
        arr[v] = [0, 0]     # 방문했으면 다시 탐색하지 않도록 초기화
    print(f'#{tc} {cnt}')