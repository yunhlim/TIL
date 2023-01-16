def recur(cur, a_goals, b_goals, per):
    # 반복해서 계산하는 값인지 확인
    if dp[cur][a_goals][b_goals] != -1:
        return dp[cur][a_goals][b_goals]

    # 90분이 다 지나간 경우
    if cur == 18:
        # 둘중 하나라도 소수인지 확인
        if a_goals in sosus or b_goals in sosus:
            return per
        else:
            return 0

    ans = 0
    # 경우의 수 4가지
    # 둘 다 골 못 넣는 경우
    ans += recur(cur + 1, a_goals, b_goals, per *
                 (100 - a_per) * (100 - b_per))
    # a만 골 넣는 경우
    ans += recur(cur + 1, a_goals + 1, b_goals, per * a_per * (100 - b_per))
    # b만 골 넣는 경우
    ans += recur(cur + 1, a_goals, b_goals + 1, per * (100 - a_per) * b_per)
    # 둘 다 골 넣는 경우
    ans += recur(cur + 1, a_goals + 1, b_goals + 1, per * a_per * b_per)

    # dp에 값 저장
    dp[cur][a_goals][b_goals] = ans
    return ans


a_per = int(input())
b_per = int(input())
sosus = [2, 3, 5, 7, 11, 13, 17]
dp = [[[-1] * 19 for _ in range(19)] * 19 for _ in range(19)]
print(recur(0, 0, 0, 1) / (100 ** 36))
