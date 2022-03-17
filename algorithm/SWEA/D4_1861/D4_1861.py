# from collections import deque


# def check(y, x):    # 현재 위치에서 최대 이동 횟수를 찾는다.
#     cnt = 1     # 이동 횟수, default가 1
#     num = arr[y][x]
#     queue = deque()
#     queue.append([y, x])
#     while queue:
#         y, x = queue.popleft()
#         for i in range(4):  # 4방향 탐색
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny < n and 0 <= nx < n: 
#                 if abs(arr[ny][nx] - arr[y][x]) == 1:    # 1 크거나 같은 경우
#                     if arr[ny][nx] - arr[y][x] == -1: # 1 더 작은 경우
#                         num = arr[ny][nx]             # 시작점 변경
#                     cnt += 1
#                     queue.append([ny, nx])
#         arr[y][x] = -1
#     return cnt, num


# t = int(input())
# dy = [0, 1, 0, -1]  # 우 하 좌 상
# dx = [1, 0, -1, 0]
# for tc in range(1, t + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     room = 0        # 방 번호
#     max_cnt = 0     # 이동 횟수
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] != -1:
#                 cnt, num = check(i, j)
#                 if cnt > max_cnt or (cnt == max_cnt and num < room):
#                     room = num
#                     max_cnt = cnt
                
#     print(f'#{tc}', room, max_cnt)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    room_arr = [[-1, -1] for _ in range(n * n + 2)]   # 방 번호 배열, 앞 뒤로 패딩을 넣어준다.(앞 패딩은 방번호가 1부터 시작)

    for i in range(n):      # 방 번호 배열에 좌표를 담는다.
        for j in range(n):
            room_arr[arr[i][j]] = [i, j]

    room = 0        # 방 번호
    max_cnt = 0     # 이동 횟수
    cnt = 1         # 현재 이동 횟수
    for i in range(1, n * n + 1):   # 마지막까지 차이가 1이면 max_cnt를 확인하지 않으니, 끝에 패딩을 넣어준 것까지 비교한다.
        if abs(room_arr[i][0] - room_arr[i + 1][0]) + abs(room_arr[i][1] - room_arr[i + 1][1]) == 1:
            if cnt == 1:    # 시작점 표시
                start = i
            cnt += 1
        else:
            if max_cnt < cnt:   # 이동 횟수가 더 클 때
                max_cnt = cnt
                room = start
            cnt = 1

    print(f'#{tc} {room} {max_cnt}')