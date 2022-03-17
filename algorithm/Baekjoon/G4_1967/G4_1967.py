import sys
sys.setrecursionlimit(10000)    # 재귀 깊이를 늘린다.

def recur(n):
    global total_max
    if arr[n] == []:        # 자식 노드가 없으면 0을 반환
        return 0
    
    result = []
    for c, w in arr[n]:     # 자식 노드를 재귀호출하면서 가중치 값을 더해준다.
        result.append(w + recur(c))

    result.sort()           # 노드에 연결된 길이들을 크기 순대로 정렬한다.
    result = result[::-1][0:2]      # 가장 긴 2개만 남긴다.
    total_max = max(total_max, sum(result))  # 2개를 합한 것이 현재 구한 최대 트리의 지름보다 큰지 확인
        

    return result[0]        # 노드에 연결된 선 중 가장 긴 길이를 리턴


n = int(input())
arr = [[] for _ in range(n + 1)]    # 부모 노드를 인덱스로 하는 리스트(자식노드와 가중치를 담는다.)

for i in range(n - 1):
    p, c, w = map(int, input().split())
    arr[p].append([c, w])   # 부모 노드의 리스트에 자식 노드와 그 때의 가중치를 리스트로 담는다.

total_max = 0   # 가장 긴 트리의 지름
recur(1)
print(total_max)