T = int(input())
for _ in range(T):
    k, n = map(int, input().split()) # k는 보트가 원하는 무게, n은 각 반당 인원
    arr = [list(map(int, input().split())) for _ in range(4)] # 4 반의 학생들의 몸무게
    arr_1 = []
    arr_2 = []

    for i in range(n):
        for j in range(n):
            arr_1.append(arr[0][i] + arr[1][j])
            arr_2.append(arr[2][i] + arr[3][j])
    arr_1.sort()
    arr_2.sort()
    
    s = 0
    e = len(arr_1) - 1
    result = arr_1[s] + arr_2[e]
    while s < len(arr_1) and e >= 0:
        ssum = arr_1[s] + arr_2[e]
        if abs(k - result) > abs(k - ssum):
            result = ssum
        elif abs(k - result) == abs(k - ssum):
            result = min(ssum, result)
        
        if ssum < k:
            s += 1
        elif ssum > k:
            e -= 1
        else:
            break
    print(result)