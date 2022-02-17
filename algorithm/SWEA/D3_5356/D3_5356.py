# deque 활용
# from collections import deque

# T = int(input())
# for tc in range(1, 1+T):
#     arr = [deque(input()) for _ in range(5)]
#     result = ''
#     while True:
#         cnt = 0
#         for i in range(5):
#             if len(arr[i]):
#                 result += arr[i].popleft()   
#                 cnt += 1
#         if cnt == 0: break
#     print(f'#{tc} {result}')



T = int(input())
for tc in range(1, 1+T):
    arr = [list(input()) for _ in range(5)]
    result = ''
    while True:
        cnt = 0
        for i in range(5):
            if len(arr[i]):
                result += arr[i][0]
                del arr[i][0]
                cnt += 1
        if cnt == 0: break
    print(f'#{tc} {result}')