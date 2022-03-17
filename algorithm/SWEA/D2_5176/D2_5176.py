def in_order(v):    # 완전 이진 트리 탐색(중위 순회)
    global cnt, result
    if v <= n:      # n까지 확인
        in_order(v * 2)
        cnt += 1    # 확인할 때마다 cnt + 1
        if v == 1:  # 조상 노드 값 담기
            result[0] = cnt
        elif v == n // 2:   # 조상 노드 // 2 값 담기
            result[1] = cnt
        in_order(v * 2 + 1)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    cnt = 0     # 노드에 저장된 값
    result = [0, 0]     # 루트 노드에 저장된 값, n // 2 노드에 저장된 값
    in_order(1)
    print(f'#{tc}', *result)