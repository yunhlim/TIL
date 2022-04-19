n = int(input())
arr = sorted(list(map(int, input().split())))
result = abs(arr[0] + arr[1] + arr[2])  # 비교하기 위한 값, 배열 앞에서 3개 선택하여 더한 후 절댓값을 넣는다.
result_arr = [arr[0], arr[1], arr[2]]   # 배열에 세 수를 담아준다.
for i in range(n):  # 하나를 우선 선택한다.
    a = arr[i]  # 하나 선택
    s = 0       # 투포인터
    e = n - 1
    while s < e:    # 같지 않을 때만 봐야 한다.
        if s == i:  # 선택한 값을 중복 선택하지 않기 위함
            s += 1
            continue
        if e == i:
            e -= 1
            continue
        if abs(a + arr[s] + arr[e]) < result:   # 이전에 구한 값보다 작은 경우만
            result = abs(a + arr[s] + arr[e])   # 세 수의 합의 절댓값을 초기화
            result_arr = [a, arr[s], arr[e]]    # 출력해야하니 배열에 담는다.
        if a + arr[s] + arr[e] == 0:
            print(*sorted([a, arr[s], arr[e]])) # 합이 0이면 바로 출력한다.
            exit()
        elif a + arr[s] + arr[e] > 0:           # 합이 0보다 큰 경우 큰 값을 줄인다.
            e -= 1
        else:                                   # 합이 0보다 작으면 작은 값을 키운다.
            s += 1

print(*sorted(result_arr))      # 세 수를 정렬해 작은 수부터 출력한다.