from collections import deque


n, m = map(int, input().split())
graph = [set() for _ in range(n + 1)]       # 현재 가수 다음에 나올 가수들의 집합
in_degree = [set() for _ in range(n + 1)]   # 현재 가수 이전에 나와야 할 가수들의 집합(다 담고 길이로 바꿔줄 예정)

for i in range(m):
    temp = list(map(int, input().split()))      # PD가 정한 순서
    for i in range(1, len(temp)):
        graph[temp[i]] = graph[temp[i]] | set(temp[i + 1:])     # 다음에 나올 가수들 합집합
        in_degree[temp[i]] = in_degree[temp[i]] | set(temp[1:i])    # 이전에 나올 가수들 합집합

que = deque()                   # 순서에 따라 가수들을 담을 큐
for i in range(1, n + 1):
    in_degree[i] = len(in_degree[i])        # 집합을 길이로 바꿔 위상 정렬
    if in_degree[i] == 0:       # 위상이 0인(가장 먼저 나와도 되는 가수) 가수를 먼저 담는다.
        que.append(i)

result = []                     # 순서대로 출력할 result 배열(순서를 정하는게 불가능한 경우를 대비)
while que:
    cur = que.popleft()         # 위상이 0인 가수들을 pop
    result.append(cur)          # result에 가수들을 담아준다.
    for nxt in graph[cur]:      # 현재 가수 이후에 나오는 가수들을 순회
        in_degree[nxt] -= 1     # 다음에 나오는 가수들의 위상을 1씩 줄여준다.
        if in_degree[nxt] == 0: # 위상이 0인 가수들을 큐에 담는다.
            que.append(nxt)

if len(result) != n:            # 불가능한 경우
    print(0)
else:                           # 가능한 경우
    for singer in result:
        print(singer)