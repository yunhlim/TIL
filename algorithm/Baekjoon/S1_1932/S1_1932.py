import sys
input = sys.stdin.readline


def recur(cur, i):  # 탑다운 백트래킹
    global max_result
    if cur == n:    # 끝까지 확인했으면 0을 리턴
        return 0

    if dp[cur][i] == -1:    # 계산하지 않았을 때
        dp[cur][i] = arr[cur][i] + max(recur(cur + 1, i), recur(cur + 1, i + 1))

    return dp[cur][i]   # 계산한 경우 바로 리턴


n = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * i for i in range(1, n + 1)]    # 똑같은 계산과정은 반복하지 않는다.
print(recur(0, 0))