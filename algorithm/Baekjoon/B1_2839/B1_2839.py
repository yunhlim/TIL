def bongji(N):  # 최소로 가져갈 수 있는 봉지의 수
    cnt = 0    # 봉지의 수
    for i in range(0, N + 1, 3):            # 3개를 담는 봉지를 0개부터 증가
        if (N - i) % 5 == 0:                # 5개로 나누어떨어지는지 확인
            return cnt + ((N - i) // 5)       # 3개를 담은 봉지 + 5개를 담은 봉지
        cnt += 1    # 3개를 담을 때마다 1 증가
    return -1


print(bongji(int(input())))