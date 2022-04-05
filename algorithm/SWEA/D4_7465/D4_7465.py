def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x]) # 경로 압축
    return parent[x]


def union(a, b):
    p_a = find(a)
    p_b = find(b)
    if p_a < p_b:           # 수가 작은 것으로 root를 합쳐나간다.
        parent[p_b] = parent[p_a]
    else:
        parent[p_a] = parent[p_b]


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())

    parent = [i for i in range(n + 1)]      # 각 정점들을 자신의 값으로 root를 초기화한다.
    for i in range(m):
        v1, v2 = map(int, input().split())  # 입력으로 받은 연결된 두 정점
        if find(v1) == find(v2):    # root가 같으면 continue
            continue
        union(v1, v2)       # root가 다르면 합쳐준다.

    root = set()
    for i in range(1, n + 1):   # root의 총 개수를 찾는다.(연결 요소의 개수)
        root.add(find(i))

    print(f'#{tc} {len(root)}')