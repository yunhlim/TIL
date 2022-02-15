T = int(input())
A = list(range(1, 13))    # A: [1,2,...,12]
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N:부분집합 원소의 수, K:부분 집합의 합
    result_sum = 0 # 만족시키는 부분집합 개수
    for i in range(1 << 12): # 모든 부분집합 탐색
        cnt = 0
        sum_num = 0
        for j in range(12):
            if i & (1 << j):
                sum_num += A[j]
                cnt += 1
        if cnt == N and sum_num == K:
            result_sum += 1 # 만족시키는 경우 + 1

    print(f'#{tc} {result_sum}')
