# 백만 장자 프로젝트

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    p_arr = list(map(int, input().split())) # 날짜별 가격을 담은 배열
    p_max = 0   # 가격의 최댓값
    coin = 0 # 이익
    for i in range(N-1, -1, -1):    # 뒤에서부터 최대값을 찾아 현재 값과 차이를 담아준다.
        if p_max < p_arr[i]:    # 최댓값이 나오면 업데이트해주고 차이는 0으로 적어준다.
            p_max = p_arr[i]
        else: coin += p_max - p_arr[i]
    print(f'#{tc} {coin}')
