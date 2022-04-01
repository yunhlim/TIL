from collections import deque


def in_range(x):        # 범위를 나타내는 함수
    return 0 < x <= 1000000


def bfs():
    visited = [0 for _ in range(1000001)]   # 연산의 중간과정은 항상 백만 이하의 자연수
    que = deque()
    que.append(n)
    d = 0       # 연산 횟수
    while que:
        size = len(que)
        for i in range(size):
            v = que.popleft()
            if v == m:
                return d

            for i in range(3):
                if not(in_range(v + cal[i])) or visited[v + cal[i]]:
                    continue
                visited[v + cal[i]] = 1
                que.append(v + cal[i])

            if in_range(v * 2) and visited[v * 2] == 0:     # 곱하기는 따로 작성한다.
                visited[v * 2] = 1
                que.append(v * 2)
        d += 1

t = int(input())
cal = [1, -1, -10]      # +, - 계산할 것들을 담아준다.
for tc in range(1, 1 + t):
    n, m = map(int, input().split())
    print(f'#{tc} {bfs()}')