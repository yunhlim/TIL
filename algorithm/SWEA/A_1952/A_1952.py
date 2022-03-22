def recur(cur, fee):
    global min_fee
    if cur > min_fee:       # 현재 요금이 업데이트 된 최소 요금보다 비싸면 return
        return
    if cur >= 12:           # 12개월을 넘어서는 경우
        min_fee = min(min_fee, fee)     # 최소값 업데이트
        return
    if arr[cur] == 0:
        recur(cur + 1, fee)                     # 이용하지 않으면 다음 월로 이동
    else:
        recur(cur + 1, fee + min(mon, day * arr[cur]))    # 당일 요금은 이용 일만큼 곱한다.
        recur(cur + 3, fee + mon_3)             # 3달은 3달을 더해줘야 한다.


for tc in range(1, 1 + int(input())):
    day, mon, mon_3, year = map(int, input().split())
    arr = list(map(int, input().split()))
    min_fee = year      # 1년 요금은 처음에 넣고 최솟값으로 업데이트
    recur(0, 0)
    print(f'#{tc} {min_fee}')