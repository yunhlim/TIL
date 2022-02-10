T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    M_lst = list(map(int, input().split())) # 충전기 설치된 정류장
    station = [0 for _ in range(N+1)]   # 정류장 0으로 초기화

    for num in M_lst:   # 충전기가 설치되면 정류장을 1로 변경
        station[num] = 1

    now = 0 # 현재 위치
    cnt = 0 # 충전 횟수
    while now + K < N:  # 현재 충전없이 종점에 도착할 수 있는 위치에 있는지 확인
        move = 0 # 충전기 설치 구간이 있는지 확인
        for location in range(now + 1, now + K + 1):    # 최대 이동 구간
            # 최대한 멀리 있는 충전기로 이동
            if station[location] == 1:
                now = location  # 충전기로 이동
                move = 1    # 충전기 설치 구간으로 움직임 표시
        if move == 0: # 충전기 설치 구간으로 움직이지 못하는 경우
            cnt = 0 # 종점에 도착하지 못하니 0으로 출력
            break
        else: cnt += 1  # 충전했으니 cnt 증가
    print(f'#{tc} {cnt}')