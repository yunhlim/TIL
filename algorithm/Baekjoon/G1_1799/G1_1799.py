def move(x, y):     # 다음 위치로 이동
    if x == 0 or y == n - 1:      # 현재 대각선을 다 확인한 경우 다음 대각선으로 이동
        return next_row(x, y)
    else:           # 오른쪽 위로 이동
        return x - 1, y + 1


def next_row(x, y):     # 다음 대각선으로 이동
    if x + y == 2 * (n - 1):
        return 0        # 끝
    if x + y + 1 >= n:      # x + y가 n보다 크거나 같은 경우
        return n - 1, x + y - n + 2
    return x + y + 1, 0


def recur(x, y, cnt):
    global max_cnt
    # 가지치기
    if 2 * n - 1 - (x + y) + cnt <= max_cnt:     # 앞으로 비숍으로 다 채워도 현재 구한 최대값보다 작거나 같은 경우
        return
    while not arr[x][y] or visited[x-min(x, y)][y-min(x, y)]:
        nxt_x_y = move(x, y)
        if nxt_x_y:
            x, y = nxt_x_y
        else:       # 놓을 수 있는 자리를 다 확인한 경우
            max_cnt = max(max_cnt, cnt)
            return

    # 비숍을 놓으면 오른쪽 아래 대각선에 위치한 곳에 놓지 못하도록 설정
    nxt_x_y = next_row(x, y)
    if nxt_x_y:
        visited[x-min(x, y)][y-min(x, y)] = 1
        recur(nxt_x_y[0], nxt_x_y[1], cnt + 1)        # 비숍을 놓는 경우 다음 대각선으로 이동
        visited[x-min(x, y)][y-min(x, y)] = 0
    else:       # 놓을 수 있는 자리를 다 확인한 경우
        max_cnt = max(max_cnt, cnt + 1)     # 비숍을 놓은 상태로 확인
        return
    
    # 비숍을 놓지 않는 경우
    nxt_x_y = move(x, y)
    if nxt_x_y:
        x, y = nxt_x_y
    else:       # 놓을 수 있는 자리를 다 확인한 경우
        max_cnt = max(max_cnt, cnt)
        return    
    recur(x, y, cnt)    # 비숍을 놓지 않는 경우
    

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
max_cnt = 0
recur(0, 0, 0)
print(max_cnt)

# def DFS(w):
#     ch[w] = 1
#     for m in G[w]:
#         if bang[m] == 0:
#             bang[m] = w
#             return True
#         elif ch[bang[m]] == 0 and DFS(bang[m]):
#             bang[m] = w
#             return True
#     return False
# N = int(input())
# gra = [list(map(int, input().split())) for _ in range(N)]

# G = [[] for _ in range(2*N)]

# for i in range(N):
#     for j in range(N):
#         if gra[i][j] == 1:
#             G[j-i+N].append(i+j+1)


# res = 0
# bang = [0]*(2*N)
# for i in range(1, 2*N):
#     ch = [0]*(2*N)
#     if DFS(i):
#         res += 1
# print(res)