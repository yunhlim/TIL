from collections import deque


def que_add(node, nxt):         # 확인 후 visited 업데이트 및 큐에 담기
    if in_range(nxt) and visited[nxt] == []:    # 범위 체크, 방문 확인
        visited[nxt] = visited[node] + [nxt]    # 방문하지 않았으면 이전 값들을 넣어준다.
        queue.append(nxt)                       # 큐에 넣는다.


def in_range(x):                # 범위 체크
    return 0 < x <= 1000000


n = int(input())
visited = [[] for _ in range(1000001)]      # 확인한 값들을 넣어준다.
mul = [3, 2]    # 3, 2 나누기
visited[n].append(n)        # 1을 담아준다.
queue = deque()
queue.append(n)

while queue:    # BFS
    node = queue.popleft()
    if node == 1:           # n이 나왔으면 종료
        break
    for j in range(2):      # 나누기
        if node % mul[j] == 0:  # 나누어 떨어지는 경우에만
            nxt = node // mul[j]    # 나눈다.
            que_add(node, nxt)
    # -1
    nxt = node - 1
    que_add(node, nxt)

print(len(visited[1]) - 1)
print(*visited[1])