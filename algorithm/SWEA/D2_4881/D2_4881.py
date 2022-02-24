# 배열 최소 합
def recur(cur, ssum):
    global min_sum                  # 최솟값보다 현재 합이 큰지 확인하기 위해 사용
    for i in range(N):
        if visited[i] == 0:         # 나오지 않은 열의 위치일 경우
            visited[i] = 1
            ssum += arr[cur][i]
            if min_sum > ssum:      # 현재 최솟값보다 작은 경우는 종료
                if cur == N - 1:    # 다 더한 경우 최솟값인지 확인
                    min_sum = ssum
                else:
                    recur(cur + 1, ssum)    # 아직 N개가 안나왔으면 다음 열 확인
            visited[i] = 0
            ssum -= arr[cur][i]

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]     # 나왔는지 확인
    min_sum = 10 * N    # 최소 값에 가장 큰 값을 넣어 놓는다.
    recur(0, 0)     # 재귀로 해결
    print(f'#{tc} {min_sum}')


















