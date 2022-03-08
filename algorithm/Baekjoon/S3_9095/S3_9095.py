T = int(input())


def recur(cur):	# 백트래킹
    if cur < 0:		# 0을 초과했으니 나타낼 수 없다.
        return 0
        
    if cur == 0:	# 0에 도달하면 1, 2, 3으로 나타낼 수 있는 경우
        return 1     

    if dp[cur] != -1:		# 이미 확인했던 값이면 dp에서 가져다가 쓴다.
        return dp[cur]

    ret = 0
    for i in range(1, 4):
        ret += recur(cur - i)	# 재귀함수로 깊은 곳부터 갯수를 센다.

    dp[cur] = ret		# dp에 값을 저장
    return dp[cur]

dp = [-1 for _ in range(11)]

for i in range(T):
    n = int(input())
    print(recur(n))	# n부터 시작