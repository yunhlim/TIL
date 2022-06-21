import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)  # 주어진 입력이 1000000이다. 그것보다 크게 범위를 늘린다.


def recur(node):
    visited[node] = 1
    if dp[node][1]:             # dp에 값이 저장되어 있는 경우
        return dp[node]
    dp[node][1] = 1    # 현재 노드가 얼리어답터이니 1로 시작
    for v in graph[node]:  # 현재 노드에 연결된 노드 순회
        if visited[v]:  # 이미 나왔던 노드는 자식 노드가 아닌, 부모 노드
            continue
        non_early, early = recur(v)     # 자식 노드가 얼리 어답터인 경우와 아닌 경우
        dp[node][0] += early        # 현재 노드가 얼리 어답터가 아니면, 자식은 모두 얼리 어답터여아 한다.
        dp[node][1] += min(early, non_early)    # 현재 노드가 얼리 어답터이면, 자식 노드는 얼리 어답터이든 아니든 상관없다.
                                                # 따라서 작은 값으로 사용한다.
    return dp[node]
    

n = int(input())
graph = [[] for _ in range(n + 1)]      # 노드들의 연결 관계
dp = [[0, 0] for _ in range(n + 1)]     # 노드에서 최소 얼리 어답터 수(현재 노드가 얼리 어댑터가 아닌 경우와, 얼리 어댑터인 경우)
visited = [0 for _ in range(n + 1)]     # 이미 확인한 노드인지 확인하기 위한 배열
for i in range(n - 1):      # 연결 관계를 graph에 담아준다.
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
 
print(min(recur(1)))        # 1를 루트 노드로 시작