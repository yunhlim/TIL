# DP 방법 1
# n = int(input())
# memo = [[1]]            # 인덱스에는 횟수의 최솟값에 맞는 숫자들을 채운다. 0부터 순차적으로 채워나간다.
# visited = [0] * (n + 1) 
# visited[1] = 1          # 1을 담아준다.

# while visited[n] == 0:  # n이 나오면 종료
#     arr = []
#     for num in memo[-1]:    # 현재 memo의 젤 오른쪽에 담겨있는 숫자들을 사용한다.
#         if num + 1 < n + 1 and visited[num + 1] == 0:   # 1을 더한 값이 나왔는지 확인
#             visited[num + 1] = 1
#             arr.append(num + 1)
#         if num * 2 < n + 1 and visited[num * 2] == 0:   # 2를 곱한 값이 나왔는지 확인
#             visited[num * 2] = 1
#             arr.append(num * 2)
#         if num * 3 < n + 1 and visited[num * 3] == 0:   # 3을 곱한 값이 나왔는지 확인
#             visited[num * 3] = 1
#             arr.append(num * 3)
#     memo.append(arr)        # 나오지 않았던 숫자들을 다음 인덱스에 배열로 넣어준다.

# print(len(memo) - 1)    # 원하는 숫자가 나왔을 때 리스트의 맨 끝 인덱스 값을 출력

# DP 방법 2
n = int(input())
arr = [0] * (n + 1)

for i in range(2, n + 1):
    arr2 = []
    if i % 2 == 0:
        arr2.append(arr[i // 2])
    if i % 3 == 0:
        arr2.append(arr[i // 3])
    arr2.append(arr[i - 1])
    arr[i] = min(arr2) + 1

print(arr[n])



# BFS 방법
# from collections import deque


# n = int(input())
# arr = [0] * (n + 1)
# queue = deque()
# queue.append(1)

# while queue and arr[n] == 0:
#     v = queue.popleft()
#     if v + 1 < len(arr) and arr[v+1] == 0:
#         arr[v+1] = arr[v] + 1
#         queue.append(v + 1)
#     if v * 2 < len(arr) and arr[v*2] == 0:
#         arr[v*2] = arr[v] + 1
#         queue.append(v * 2)
#     if v * 3 < len(arr) and arr[v*3] == 0:
#         arr[v*3] = arr[v] + 1
#         queue.append(v * 3)

# print(arr[n])