import heapq
import sys
input = sys.stdin.readline


def insert(num, id):   # 값을 넣어준다. id값과 튜플로 넣어 서로 나왔는지 확인할 수 있게 해준다.
    heapq.heappush(min_heap, (num, id))
    heapq.heappush(max_heap, (-num, id))

def pop(num):
    if num == 1:    # 최대값을 꺼내는 경우
        while max_heap:     # 힙에 값이 있을 때
            pop_num = heapq.heappop(max_heap)
            if not visited[pop_num[1]]:     # 꺼내지 않았던 수이면 중단시킨다.
                visited[pop_num[1]] = 1     # 방문 표시
                return - pop_num[0]     # 값을 넣을 때 -를 붙였으니 제거 후 꺼낸다.
    else:          # 최소값을 꺼내는 경우
        while min_heap:
            pop_num = heapq.heappop(min_heap)
            if not visited[pop_num[1]]:
                visited[pop_num[1]] = 1
                return pop_num[0]

for i in range(int(input().rstrip())):
    n = int(input().rstrip())
    visited = [0 for _ in range(n)]     # id값이 pop했는지 확인할 카운팅 배열
    min_heap = []
    max_heap = []
    id = 0         # 각 최대 최소에서 서로 나왔는지 확인하기 위한 id
    for i in range(n):
        cal, num = input().split()
        if cal == 'I':
            insert(int(num), id)
        else:
            pop(int(num))
        id += 1
    
    result = []
    result.append(pop(1))
    if result[0]:       # 값이 존재하는 경우
        result.append(pop(-1))
        if result[1]:       # 값이 2개 이상 존재하는 경우
            print(*result)
        else:           # 값이 하나만 존재하는 경우, 최대 최소가 같으므로 2번 출력
            print(result[0], result[0])
    else:               # 값이 없는 경우
        print('EMPTY')