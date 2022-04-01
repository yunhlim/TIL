def recur(cur, total, money):       # 구간에서 최대의 액수 구하기
    global max_money
    if total > c:                   # c보다 크면 리턴
        return
    if cur == m:                    # 구간을 다 확인했으면 최댓값 갱신
        max_money = max(max_money, money)
        return
    # 조합으로 (선택하는 경우와, 선택하지 않는 경우)
    recur(cur + 1, total, money)
    recur(cur + 1, total + temp[cur], money + temp[cur] ** 2)


t = int(input())
for tc in range(1, 1 + t):
    n, m, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    moneys = [[0] * n for _ in range(n)]
    for i in range(n):      # 각 구간별 최댓값을 맨 왼쪽 인덱스에 담아준다.
        for j in range(n - m + 1):
            cnt = 0
            max_money = 0
            temp = arr[i][j:j + m]      # 구간을 배열에 담아 재귀함수로 최대 액수를 찾아준다.
            recur(0, 0, 0)
            moneys[i][j] = max_money

    max_money = []
    max_result = 0
    for i in range(n):          # 각 라인별로 최댓값을 뽑는다.
        max_money.append((max(moneys[i]), i))
    max_money.sort()            # 최댓값을 정렬한다.
    max_result = max_money[-1][0] + max_money[-2][0]        # 정렬하여 큰 순서로 2개 뽑아 더해준다.

    for i in range(1, n + 1):
        if max_money[-i][0] != max_money[-1][0]:  # 정렬한 배열 중 최댓값과 동일한 것이 여러 개 있으면 다 골라준다.  
            break
        index = max_money[-i][1]       # 확인할 라인
        for j in range(n):
            for k in range(j + m, n, m):        # 최댓값이 나오면 바꿔준다.
                max_result = max(max_result, moneys[index][j] + moneys[index][k])

    print(f'#{tc} {max_result}')