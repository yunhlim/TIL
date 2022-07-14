from collections import deque


def go(a, b):       # 갈 수 있는지 판단
    dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
    if dist <= 1000:
        return True
    else:
        return False


t = int(input())
for _ in range(t):
    n = int(input())
    house = list(map(int, input().split()))
    stores = [[] for _ in range(n)]
    for i in range(n):
        stores[i] = list(map(int, input().split()))
    festival = list(map(int, input().split()))
    visited = [0 for _ in range(n)]     # 편의점을 방문했는지 표시
    result = 'sad'
    que = deque()
    que.append(house)
    while que:
        place = que.popleft()
        if go(place, festival):
            result = 'happy'
            break
        for i in range(n):
            if visited[i]:      # 이미 방문한 편의점인지 파악
                continue
            if go(place, stores[i]):        # 갈 수 있는 편의점이 있으면 이동
                visited[i] = 1
                que.append(stores[i])
    print(result)