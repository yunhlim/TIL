T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())    # NxN 개의 퍼즐, 단어 길이 K
    arr = [list(map(int, input().split()))+[0] for _ in range(N)]   # 퍼즐의 오른쪽에 0추가
    arr += [list(0 for _ in range(N+1))]    # 퍼즐의 아래에도 0추가
    result_cnt = 0  # 특정 길이를 넣을 수 있는 개수
    # 0을 만나면 그 전에 1이 몇개 있는지 확인한다.
    # 인덱스 마지막도 확인해주기 위해 퍼즐 오른쪽, 아래로 0을 추가해주었다.
    for i in range(N):
        row_cnt = 0 # row열에서 연속된 1의 개수
        col_cnt = 0 # col열에서 연속된 1의 개수
        for j in range(N+1):
            if arr[i][j] == 0:  # 0을 만나면 그 전에 1이 연속으로 몇 개 있었는지 확인
                if row_cnt == K:    # K개 있었으면 result 증가
                    result_cnt += 1
                row_cnt = 0     # 0을 만났으니 cnt를 0으로 초기화
            else: row_cnt += 1  # 1을 만나면 cnt에 1추가
            if arr[j][i] == 0:  # 세로도 위처럼 한다.
                if col_cnt == K:
                    result_cnt += 1
                col_cnt = 0
            else: col_cnt += 1
    print(f'#{tc} {result_cnt}')