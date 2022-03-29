for tc in range(1, 1 + int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[1])    # 종료시간으로 정렬
    cnt, end = 0, 0
    for i in range(n):  # 종료시간 낮은 것부터 확인
        s, e = arr[i]
        if end <= s:  # 시작시간이 이전 종료시간보다 크거나 같으면 + 1
            end = e   # 종료시간을 업데이트
            cnt += 1
    print(f'#{tc} {cnt}')