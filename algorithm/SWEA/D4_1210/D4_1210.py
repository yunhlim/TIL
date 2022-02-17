# for _ in range(10):
#     tc = int(input())
#     ladder = [list(map(int, input().split())) for _ in range(100)]
#     dir = (-1, 0)    # 처음에는 올라간다.

#     for i in range(100):    # 아래 2를 찾고 거기서부터 올라간다!
#         if ladder[99][i] == 2:
#             X = i
#             break
#     current = (98, X)   # 99번째 줄에서 시작
#     while current[0] != 0:  # 맨 위로 올라오면 끝(0번째 인덱스)
#         ni, nj = current
#         if dir != (-1, 0):   # 움직이던 방향이 가로 방향인 경우
#             if not(0 <= nj+dir[1] < 100 and ladder[ni][nj+dir[1]]): # 가던 방향으로 움직일 수 있는지 판단
#                 dir = (-1, 0)     # 못가면 위로, 위쪽 di = -1, dj = 0 
#         else:           # 움직이던 방향이 위 방향인 경우
#             if 0 <= nj-1 < 100 and ladder[ni][nj-1]:    # 왼쪽으로 움직일 수 있는지 판단
#                 dir = (0, -1)  # 왼쪽 di = 0, dj = -1
#             if 0 <= nj+1 < 100 and ladder[ni][nj+1]:    # 오른쪽으로 움직일 수 있는지 판단
#                 dir = (0, 1)  # 오른쪽 di = 0, dj = 1
#         current = (ni+dir[0], nj+dir[1])    # 이동시킨다.
#     print(f'#{tc} {current[1]}')

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    y = 99
    for i in range(100):    # 아래 2를 찾고 거기서부터 올라간다!
        if ladder[y][i] == 2:
            x = i
            break
    
    dx = [-1, 1] # 좌우만 검색

    while y > 0:    
        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx < 100 and ladder[y][nx]:
                ladder[y][x] = 0    # 행으로 움직이면 그 전 위치를 0으로 지워버리면 쉽다.
                x = nx
                break
        else:
            y -= 1
    print(f'#{tc} {x}')