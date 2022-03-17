def recur(cur, total):  # 조합
    global result

    if result <= total:     # result보다 현재 합이 더 크면 종료
        return
    if cur == n:            # 모든 인원을 확인했으면
        if total >= top:    # top보다 크거나 같은지 확인
            result = min(result, total)     # result보다 작은지 확인
        return

    recur(cur + 1, total)   # 현재 사람을 고르는 경우
    recur(cur + 1, total + arr[cur])    # 고르지 않는 경우


t = int(input())
for tc in range(1, t+1):
    n, top = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 10000 * n      # 키가 최대 10000
    recur(0, 0)             # 조합으로 확인
    print(f'#{tc} {result - top}')     # 차이를 출력