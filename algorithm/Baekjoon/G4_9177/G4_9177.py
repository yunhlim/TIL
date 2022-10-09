# 단어 섞기
# 딕셔너리 DP
def dfs(cur, idx1, idx2):
    if cur == len(result):
        return True

    if dp.get(f'{idx1},{idx2}') is not None:
        return dp[f'{idx1},{idx2}']

    ans = 0
    if idx1 < len(string1) and result[cur] == string1[idx1]:
        if dfs(cur + 1, idx1 + 1, idx2):
            ans = 1

    if idx2 < len(string2) and result[cur] == string2[idx2]:
        if dfs(cur + 1, idx1, idx2 + 1):
            ans = 1

    dp[f'{idx1},{idx2}'] = ans
    return ans


n = int(input())

for tc in range(1, n + 1):
    string1, string2, result = input().split()
    dp = {}
    print(f"Data set {tc}:", 'yes' if dfs(0, 0, 0) else 'no')

# 탑다운 DP
# def dfs(cur, idx1, idx2):
#     if cur == len(result):
#         return True

#     # 확인했던 값 들어온 경우
#     if dp[idx1][idx2] != -1:
#         return dp[idx1][idx2]

#     ans = 0
#     if idx1 < len(string1) and result[cur] == string1[idx1]:
#         if dfs(cur + 1, idx1 + 1, idx2):
#             ans = 1

#     if idx2 < len(string2) and result[cur] == string2[idx2]:
#         if dfs(cur + 1, idx1, idx2 + 1):
#             ans = 1

#     dp[idx1][idx2] = ans
#     return ans


# n = int(input())

# for tc in range(1, n + 1):
#     string1, string2, result = input().split()
#     dp = [[-1 for _ in range(len(string2) + 1)]
#           for _ in range(len(string1) + 1)]
#     print(f"Data set {tc}:", 'yes' if dfs(0, 0, 0) else 'no')
