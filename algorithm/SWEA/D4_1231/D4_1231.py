def in_order(v):
    global last
    if v <= last:
        return in_order(v*2) + tree[v] + in_order(v*2+1)    # 완전 이진트리의 중위순회 방법
    else:
        return ''


for tc in range(1, 11):
    n = int(input())
    tree = [0 for _ in range(n + 1)]
    last = 0
    for i in range(1, n + 1):
        tree[i] = input().split()[1]    # 트리에 값을 넣는다. 완전이진트리니 순서대로 넣어 구현
        last += 1
    print(f'#{tc} {in_order(1)}')