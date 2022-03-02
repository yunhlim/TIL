from collections import deque


n = int(input())    # 컴퓨터 수
e = int(input())    # 간선의 수
arr = [[] for _ in range(n + 1)]   # 정점들의 연결관계

for i in range(e):
    a, b = map(int, input().split())    # 연결된 컴퓨터의 숫자 a, b
    arr[a].append(b)
    arr[b].append(a)    # 방향이 없는 그래프니 반대방향도 넣어준다.

visited = [0] * (n + 1) # 방문 했는지 확인
queue = deque()
queue.append(1)         # 바이러스의 시작점 1을 큐에 담는다.

cnt = 0
while queue:                # 큐에 값이 있으면 반복문을 돈다.
    v = queue.popleft()     # 정점을 하나씩 꺼낸다.
    if visited[v] == 0:     # 정점이 아직 나오지 않았으면 확인
        cnt += 1            # 바이러스가 퍼진 컴퓨터의 개수를 하나 더한다.
        visited[v] = 1      # 확인했음을 표시
        for v2 in arr[v]:   # 연결되어있는 컴퓨터를 큐에 담아준다.
            queue.append(v2)

print(cnt - 1)      # 바이러스가 전염된 컴퓨터의 개수를 출력