def find(x):            # root 찾기
    if root[x] != x:
        root[x] = find(root[x])     # 경로 압축 : 부모가 중간에 바꼈을 때 전부다 root로 직접 연결시켜준다.
    return root[x]


def union(a, b):       # 병합
    r_a = find(a)       # a의 root
    r_b = find(b)       # b의 root
    if r_a < r_b:       # 큰 root를 더 작은 root로 바꾼다.
        root[r_b] = r_a
    else:
        root[r_a] = r_b


t = int(input())
for tc in range(1, 1 + t):
    n = int(input())
    arr_x = list(map(int, input().split()))
    arr_y = list(map(int, input().split()))
    e = float(input())
    edges = []

    for i in range(n):
        x1, y1 = arr_x[i], arr_y[i]
        for j in range(i + 1, n):
            x2, y2 = arr_x[j], arr_y[j]
            edges.append([(x1 - x2) ** 2 + (y1 - y2) ** 2, i, j])    # 거리와 노드들을 리스트에 담는다.
    edges.sort()    # 거리로 정렬
    root = [i for i in range(n)]
    cnt = 0         # 연결된 간선의 개수
    result = 0      # 출력할 거리 제곱의 합

    for i in range(len(edges)):
        if cnt == n - 1:            # 트리를 모두 연결한 경우
            break
        d, n1, n2 = edges[i]
        if find(n1) != find(n2):    # root가 다른 경우
            union(n1, n2)           # 합쳐준다.
            cnt += 1                # 연결한 간선의 개수를 +1
            result += d
    
    print(f'#{tc} {int(result * e + 0.5)}')     # 마지막에 e를 곱한다. 반올림이니 0.5를 더하고 정수형변환