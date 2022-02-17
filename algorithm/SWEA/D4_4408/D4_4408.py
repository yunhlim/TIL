def room_number(number):    # 짝수와 홀수번째 방이 같은 라인에 있으면 같은 숫자로 변환
    new_number = int(number)
    if new_number % 2:
        new_number = (new_number + 1) // 2
    else:
        new_number = new_number // 2
    return new_number


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(room_number, input().split())) for _ in range(N)]
    cnt_lst = [0 for _ in range(201)]
    for i in range(N):  # 지나는 경로를 cnt_lst에 전부 1씩 더해준다.
        if rooms[i][0] < rooms[i][1]:
            for j in range(rooms[i][0], rooms[i][1] + 1):
                cnt_lst[j] += 1
        else:
            for j in range(rooms[i][1], rooms[i][0] + 1):
                cnt_lst[j] += 1
    cnt_lst = set(cnt_lst)
    max_cnt = 0
    for cnt in cnt_lst: # 겹치는 경로 중 가장 많은 경로만큼이 최저 시행 횟수이다.
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')