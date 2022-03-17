def recur(v):  # 빈 노드들을 채워준다.(후위 순회)
    if v <= n:
        if tree[v] == 0:    # 노드에 값이 없는 경우
            tree[v] = recur(v*2) + recur(v*2+1)
        return tree[v]      # 노드에 값이 있는 경우
    else:       # 노드의 범위를 넘어간 경우 0
        return 0


t = int(input())
for tc in range(1, t + 1):
    # n: 노드 수 m: 리프 노드 수 l: 출력할 노드 번호
    n, m, node = map(int, input().split())
    tree = [0 for _ in range(n + 1)]

    for i in range(m):  # 리프 노드를 채워준다.
        p, c = map(int, input().split())
        tree[p] = c
        
    recur(1)    # 모든 노드들 다 채우기
    print(f'#{tc} {tree[node]}')
