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