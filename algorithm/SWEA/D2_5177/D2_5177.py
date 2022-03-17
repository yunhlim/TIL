def enq(num):   # 최소 힙에 값 넣기
    global last
    last += 1       # 최소 힙에 들어간 값의 개수를 세준다.
    min_heap[last] = num    # 맨 마지막에 값을 넣어준다.
    c = last
    p = c // 2
    while p > 0 and min_heap[p] > min_heap[c]:  # 조상이 더 크면 바꾼다.
        min_heap[p], min_heap[c] = min_heap[c], min_heap[p]
        c = p
        p = c // 2


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    last = 0
    min_heap = [0] * (n + 1)    # 최소 힙 배열
    for num in arr:             # 최소 힙에 입력을 다 넣어준다.
        enq(num)
    
    # 조상 노드의 합 구하기
    anc = last // 2             # 조상 노드
    total = 0                   # 조상 노드의 합
    while anc:
        total += min_heap[anc]  # 조상 노드의 값 더하기
        anc //= 2               # 더 상위의 조상 노드로
    print(f'#{tc} {total}')