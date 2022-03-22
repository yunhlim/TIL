n = int(input())
arr = [0 for _ in range(n + 1)]
sosu = []
for i in range(2, n + 1):       # 에라토스테네스의 체 소수 판정
    if arr[i]:                  # 합성수일 땐 보지 않는다.
        continue
    sosu.append(i)              # 소수들은 sosu 리스트에 담는다.
    for j in range(i * i, n + 1, i):    # 소수의 배수들을 다 합성수 처리
        arr[j] = 1

s, e, cnt = 0, 0, 0
if sosu:                        # 소수가 없는 경우 0 출력
    sum_sosu = sosu[0]
    while s <= e:               # s가 e를 넘는 경우는 더 이상 원하는 값이 존재하지 않는다.
        if sum_sosu > n:        # 현재 합이 더 큰 경우
            sum_sosu -= sosu[s] # s를 움직여주고 왼쪽의 수를 뺀다.
            s += 1
        else:                   # 현재 합이 작거나 같은 경우
            if sum_sosu == n:   # 같으면 cnt를 증가
                cnt += 1
            e += 1              # 합이 같거나 작을 때 e를 움직인다.(같을 땐 e나 s 둘 중 뭘 움직여도 상관 X)
            if e == len(sosu):  # 인덱스를 넘으면 종료
                break
            sum_sosu += sosu[e] # e가 움직이면 더해준다.
print(cnt)