from collections import deque


def dfs(node):              # 이동
    if arr[node]:           # 이동한 노드에 사다리나 뱀이 있는 경우
        node = dfs(arr[node])           # 이동시킨다.
    if visited[node]:       # 확인했던 번호인지 체크
        return False
    else:
        return node


n, m = map(int, input().split())        # n : 사다리 개수, m : 뱀 개수
visited = [0 for _ in range(110)]
arr = [0 for _ in range(110)]           # 현재 칸에서 이동하는 좌표를 적는다. 없는 경우는 0
for _ in range(n + m):
    x, y = map(int, input().split())
    arr[x] = y

que = deque()
que.append(1)
visited[1] = 1
cnt = 0
while que:
    for _ in range(len(que)):   # 현재 같은 레벨만큼만 시행
        v = que.popleft()
        if v == 100:
            print(cnt)
            exit()
        for i in range(1, 7):
            nxt = dfs(v + i)
            if nxt:
                visited[nxt] = 1
                que.append(nxt)
    cnt += 1