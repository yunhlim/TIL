from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0 for _ in range(n + 1)]
arr = [set() for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    if e not in arr[s]:     # 같은 입력이 들어올 수 있으니 처리
        in_degree[e] += 1   # 연결된 정점들의 위상을 +1
        arr[s].add(e)

queue = deque()
for i in range(1, n + 1):   # 위상이 0인 값들을 큐에 담는다.
    if in_degree[i] == 0:
        queue.append(i)

result = []
while queue:                # 큐에는 위상이 0인 값들만 들어온다.
    v = queue.popleft()
    result.append(v)        # 결과 리스트에 순차적으로 넣어준다.
    for v2 in arr[v]:       # 연결된 정점들을 순회
        in_degree[v2] -= 1  # 위상을 -1
        if in_degree[v2] == 0:  # 위상이 0이면 큐에 담는다.
            queue.append(v2)
print(*result)