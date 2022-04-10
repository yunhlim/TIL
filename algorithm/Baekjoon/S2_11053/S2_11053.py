n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], 1 + dp[j])
            
print(max(dp))

# 탑다운 DP
# import sys
# sys.setrecursionlimit(10000)

# def recur(x, y):
#     if x < 0 or y < 0:	# 배열의 왼쪽과 위쪽을 초과한 경우 0을 리턴
#         return 0
#     if dp[x][y] != -1:	# dp에 값이 있는 경우는 있는 값 리턴
#         return dp[x][y]
#     ret = 0
#     if arr2[x] == arr[y]:	# x와 y값이 같은 경우
#         ret = max(recur(x - 1, y - 1) + 1, recur(x - 1, y))	# 왼쪽 위 대각선에 1을 더한 값과 위쪽 값을 비교 
#     else:	# x와 y값이 다른 경우
#         ret = max(recur(x, y - 1), recur(x - 1, y))	# 왼쪽과 위쪽을 비교
#     dp[x][y] = ret
#     return ret


# n = int(input())
# arr = list(map(int, input().split()))
# arr2 = sorted(set(arr))	# 중복 제거 후 정렬
# m = len(arr2)
# dp = [[-1] * n for _ in range(m)]	# 확인하는 값을 적어준다.
# print(recur(m - 1, n - 1))