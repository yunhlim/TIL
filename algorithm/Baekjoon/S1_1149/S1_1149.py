# 백트래킹 시간 초과
# import sys
# input = sys.stdin.readline


# def recur(cur, total):
#     global total_min
#     if cur == n:
#         if total < total_min:
#             total_min = total
#         return
#     if total_min < total:
#         return

#     for i in range(3):
#         if cur == 0 or i != visited[cur - 1]:
#             visited[cur] = i
#             recur(cur + 1, total + rgb[cur][i])
#             visited[cur] = 0


# n = int(input().rstrip())
# rgb = [list(map(int, input().split())) for _ in range(n)]
# visited = [0 for _ in range(n)]
# total_min = 1000 * n
# recur(0, 0)
# print(total_min)

# DFS 시간 초과
# from collections import deque
# import sys
# input = sys.stdin.readline


# def dfs(n):
#     total_min = 1000 * n
#     stack = deque()
    
#     for i in range(3):
#         stack.append((0, i, rgb[0][i]))

#     while stack:
#         v = stack.pop()
#         if v[0] == n - 1:
#             if v[2] < total_min:
#                 total_min = v[2]
#             continue
#         if total_min < v[2]:
#             continue

#         for i in range(3):
#             if v[1] != i:
#                 stack.append((v[0] + 1, i, v[2] + rgb[v[0] + 1][i]))
#     return total_min


# n = int(input().rstrip())
# rgb = [list(map(int, input().split())) for _ in range(n)]
# print(dfs(n))

# DP 방법
import sys
input = sys.stdin.readline


n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):   # 칠할 집들
    for j in range(3):  # 각 색칠한 집의 최소 값
        min_rgb = 1000000
        for k in range(3):  # 이전에 칠했던 집들 확인
            if j != k:      # 이전의 집과 색이 다른 것만 확인
                if min_rgb > rgb[i-1][k]:   # 최소값 찾기
                    min_rgb = rgb[i-1][k]
        rgb[i][j] += min_rgb    # 최소값을 더해준다.

print(min(rgb[n-1]))