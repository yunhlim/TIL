from collections import deque

for _ in range(10):
    tc = int(input())
    queue = deque(map(int, input().split()))

    cnt = 0
    while queue[-1]:    # 큐의 끝이 0이면 종료
        cnt %= 5    # 1, 2, 3, 4, 5 로 나누게 설정
        cnt += 1
        
        right = queue.popleft() - cnt   # 왼쪽에서 꺼낸 후 연산한다.
        if right > 0:                   # 오른쪽에 넣어준다.
            queue.append(right)
        else:                           # 0보다 작거나 같으면 0을 넣어준다.
            queue.append(0)
    
    print(f'#{tc}', *queue)