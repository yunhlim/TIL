import sys
sys.setrecursionlimit(5000)

def recur(x, y):
    if x < 0 or y < 0:  # 문자열의 범위를 넘어서면 공백 리턴
        return ''
    if dp[x][y] != -1:  # dp에 있는지 확인
        return dp[x][y]

    result = ''
    up = recur(x - 1, y)
    if s1[x] == s2[y]:      # 왼쪽 위 값에 문자를 더해준다.
        left = recur(x - 1, y - 1) + s1[x]
    else:                   # 왼쪽 값
        left = recur(x, y - 1)
    if len(left) < len(up): # 길이가 큰 값으로 넣는다.(같을 땐 어떻게 처리해도 상관 없다.)
        result = up
    else:
        result = left
    dp[x][y] = result   # dp에 값을 넣어준다.
    return result


s1 = input()
s2 = input()
dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))] # s1의 문자열을 하나씩 골라 s2를 확인
ans = recur(len(s1) - 1, len(s2) - 1)
print(len(ans))
if len(ans):        # 길이가 0이면 출력하지 않는다.
    print(ans)