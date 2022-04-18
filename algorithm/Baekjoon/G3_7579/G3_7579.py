def recur(cur, y):
    if y < 0:       # 비용이 0보다 작은 값은 memory를 더해도 0보다 작게 아주 작은 값을 리턴
        return -10000000
    if cur < 0:     # 아무것도 없을 땐, 0에서 출발
        return 0

    if dp[cur][y] != -1:    # dp가 채워진 경우
        return dp[cur][y]
    
    memory = memories[cur]
    fee = fees[cur]
    ret = max(recur(cur - 1, y), recur(cur - 1, y - fee) + memory)

    dp[cur][y] = ret
    return ret


n, m = map(int, input().split())
memories = list(map(int, input().split()))
fees = list(map(int, input().split()))
total_fees = sum(fees)      # 나올 수 있는 최대 비용
dp = [[-1] * (total_fees + 1) for _ in range(n)]    # 개수 x 비용인 dp 테이블

for i in range(total_fees + 1)[::-1]:   # dp 테이블의 맨 뒤부터 채운다.
    if dp[n-1][i] == -1:    # dp가 어느정도 채워지는지 확인할 수 없으니 채워졌는지 확인하고 재귀를 돌린다.
        recur(n - 1, i)
    if dp[n-1][i] < m:      # m보다 작은 값이 처음 나오는 순간을 찾는다.
        print(i + 1)        # 작은 값이 아니던 가장 작은 값 출력
        break