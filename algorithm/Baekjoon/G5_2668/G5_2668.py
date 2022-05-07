def dfs(x):            # 순환되는지 확인
    global s
    visited.append(x)
    if graph[x] not in visited:     # 새로운 값이 나오면 연결된 다음 그래프 탐색
        dfs(graph[x])
    elif graph[x] == s and graph[x] in visited:  # 시작점이 또 나왔으면 종료
        result.append(s)        # 시작점을 result 배열에 담는다.


n = int(input())
graph = [0 for _ in range(n + 1)]     # 위에서 아래 방향으로 하나씩 연결

for i in range(1, n + 1):       # 첫째줄에서 둘째줄로 연결 관계 표시
    graph[i] = int(input())

result = []         # 싸이클을 이루는 시작점을 담는다.
for s in range(1, n + 1):
    visited = []        # 부모 노드를 탐색하며 값을 담아줄 visited 배열
    dfs(s)
        
print(len(result))      # result의 길이
for i in sorted(result):        # result를 정렬 후 순서대로 출력
    print(i)