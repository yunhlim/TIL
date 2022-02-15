T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)] # 파리들이 들어있는 리스트
    max_sum = 0
    for i in range(N-M+1):  # 탐색할 MxM의 맨 위 인덱스를 택한다.
        for j in range(N-M+1):
            sum_fly = 0
            for k in range(M):  # 고른 인덱스를 중심으로 MxM의 네모 영역의 합을 구한다.
                for l in range(M):
                    sum_fly += flies[i+k][j+l]
            if max_sum < sum_fly:
                max_sum = sum_fly
    print(f'#{tc} {max_sum}')