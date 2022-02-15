# T = 10
# for tc in range(1, T+1):
#     N = int(input())    # 덤프 횟수
#     box_cnt_lst = list(map(int, input().split()))   # 박스 개수 담은 list
#     for _ in range(N):    # 평탄화 작업 + min, max 작업
#         max_cnt = box_cnt_lst[0]  # 최대 상자 수
#         min_cnt = box_cnt_lst[0]  # 최소 상자 수
#         max_idx = 0  # 최대 상자가 있는 인덱스의 값
#         min_idx = 0  # 최소 상자가 있는 인덱스의 값

#         for i in range(100):    # min, max 찾고, 평탄화 작업
#             if max_cnt < box_cnt_lst[i]:    # max 찾기
#                 max_idx = i                 # max 상자의 인덱스 값  저장
#                 max_cnt = box_cnt_lst[i]    # max 상자의 개수 저장
#             elif min_cnt > box_cnt_lst[i]:  # min 찾기, max와 동일
#                 min_idx = i
#                 min_cnt = box_cnt_lst[i]

#         if max_cnt - min_cnt < 2:   # min, max 차이가 2 이하면 평탄화 작업 중단
#             break

#         box_cnt_lst[max_idx] -= 1   # 평탄화 작업
#         box_cnt_lst[min_idx] += 1
#     else:   # 평탄화 작업을 하고 마무리 됐으니 마지막에 최대 최소를 한번 더 구한다.
#         max_cnt = box_cnt_lst[0]    # 최대 최소만 구하는 작업
#         min_cnt = box_cnt_lst[0]
#         max_idx = 0
#         min_idx = 0
#         for i in range(100):
#             if max_cnt < box_cnt_lst[i]:
#                 max_idx = i
#                 max_cnt = box_cnt_lst[i]
#             elif min_cnt > box_cnt_lst[i]:
#                 min_idx = i
#                 min_cnt = box_cnt_lst[i]

#     print(f'#{tc} {max_cnt - min_cnt}')

T = 10
for tc in range(1, T+1):
    N = int(input())    # 덤프 횟수
    boxes = list(map(int, input().split()))   # 박스를 담은 list
    height_cnt = [0 for _ in range(101)]    # 박스 높이의 개수를 담은 list
    max_height = 0
    min_height = 101
    for box in boxes: # 박스 높이에 대한 개수가 몇 개 있는지 넣어준다.
        height_cnt[box] += 1
        if box > max_height:
            max_height = box
        if box < min_height:
            min_height = box

    for _ in range(N):  # 평탄화 시작
        if max_height - min_height < 2:   # min, max 차이가 2 이하면 평탄화 작업 중단
            break
        height_cnt[max_height] -= 1       # 평탄화 작업
        height_cnt[max_height-1] += 1
        height_cnt[min_height] -= 1
        height_cnt[min_height+1] += 1
        if height_cnt[max_height] == 0:
            max_height -= 1
        if height_cnt[min_height] == 0:
            min_height += 1

    print(f'#{tc} {max_height - min_height}')