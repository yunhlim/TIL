import sys
input = sys.stdin.readline


n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
result = 0
meeting.sort(key=lambda x : (x[1], x[0]))   # 두 번째 인덱스로 먼저 정렬하고, 그 후 첫 번째 인덱스로 정렬한다.

# 끝나는 시간이 빠른 것으로 계속 찾으면 된다.
cnt = 0
e = 0
for i in range(n):
    if e <= meeting[i][0]:  # 겹치는지 확인
        cnt += 1
        e = meeting[i][1]
print(cnt)



# 첫번째 풀이
# # 최대로 진행할 수 있는 회의 수 찾기
# def recur(cur, e, cnt): # 조합 재귀로 구현(회의 인덱스, 회의 끝나는 시간, 회의 개수)
#     global max_cnt
    
#     if cur == len(stack):   # 마지막까지 탐색했으면 종료
#         max_cnt = max(max_cnt, cnt)     # 최대값인지 확인하고 바꿔준다.
#         return
#     # 가지치기: 더 진행해도 절대 답이 될 수 없으면 Stop
#     if len(stack) - cur + cnt <= max_cnt:
#         return

#     recur(cur + 1, e, cnt)  # 현재 회의를 진행하지 않는다.
#     if stack[cur][0] >= e:  # 현재 회의 시간이 이전에 진행한 회의가 끝나는 시간과 안 겹칠 때만 넣어줄 수 있다.
#         recur(cur + 1, stack[cur][1], cnt + 1)  # 다음 회의 확인, 회의 중 가장 마지막에 끝나는 시간 넣고, 회의 개수를 +1


# n = int(input())
# meeting = [list(map(int, input().split())) for _ in range(n)]
# result = 0
# meeting.sort(key=lambda x : (x[1], x[0]))   # 두 번째 인덱스로 먼저 정렬하고, 그 후 첫 번째 인덱스로 정렬한다.

# stack = []  # 빈 스택 선언
# for i in range(0, n):
#     # 현재 들어오는 회의가 이전에 있던 회의와 끝나는 시간이 같으면 범위가 더 큰 이전 걸 없앤다.
#     # 시작하는 시간과 끝나는 시간이 같으면 겹치는 것이 아니므로 같지 않을 때로 처리한다.
#     while stack and (meeting[i][1] == stack[-1][1]) and (meeting[i][0] != meeting[i][1]):
#         stack.pop() 
#     if stack and meeting[i][0] >= stack[-1][1]: # 현재 확인한 회의가 이전 회의와 전혀 겹치지 않을 때
#         max_cnt = 0
#         recur(0, 0, 0)      # stack에 있는 회의들 중 최대로 진행할 수 있는 회의 수를 찾는다.
#         result += max_cnt
#         stack = []          # stack을 초기화 한다.
#     if stack == [] or meeting[i][0] > stack[-1][0]:     # 회의 시간이 이전 것과 엇갈리게 겹치면 stack에 추가해준다.
#         stack.append(meeting[i])

# max_cnt = 0
# recur(0, 0, 0)      # stack에 남아있는 것들의 회의 수도 찾아주고 종료한다.
# print(max_cnt + result)



