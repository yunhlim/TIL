# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())    # 칠할 영역의 개수
#     arr = [[0]*10 for _ in range(10)]   # 10X10 배경
#     for _ in range(N):
#         r1, c1, r2, c2, color = map(int, input().split()) # r1,c1, r2,c2 인덱스와 color
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 if arr[i][j] == 0:   # 판에 안 칠해져있으면 0이니 color로 칠한다.
#                     arr[i][j] = color
#                 elif arr[i][j] != color:    # 서로 다른 색이면 3으로 바꾼다, 3이어도 3으로 바꾸니 상관없다.
#                     arr[i][j] = 3   # 보라색은 3으로 바꾼다.
#     purple = 0
#     for i in range(10):
#         for j in range(10):
#             if arr[i][j] == 3:
#                 purple += 1
#     print(f'#{tc} {purple}')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 칠할 영역의 개수
    arr = [[0]*10 for _ in range(10)]   # 10X10 배경
    purple = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split()) # r1,c1, r2,c2 인덱스와 color
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] == 0:   # 판에 안 칠해져있으면 0이니 color로 칠한다.
                    arr[i][j] = color
                else:   # 칠해져 있는 판에 덧칠하면 보라색으로 바뀐다.
                    purple += 1
    print(f'#{tc} {purple}')