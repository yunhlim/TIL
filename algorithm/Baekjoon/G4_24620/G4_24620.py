def search(x):
    remember = 0
    for i in range(n):
        if remember > x:
            return False
        remember += arr[i]
        if remember == x:
            remember = 0
    return True

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    mmax = 0
    ssum = 0
    zero_cnt = 0

    for i in range(n):      # 최댓값, 최솟값 구하기
        if mmax < arr[i]:
            mmax = arr[i]
        if arr[i] == 0:
            zero_cnt += 1
        ssum += arr[i]

    arr2 = []

    if mmax == 0:
        print(0)
    else:
        for i in range(1, ssum + 1):
            if i * i > ssum:                   # 제곱근 이하까지만 계산
                break
            if ssum % i == 0:
                arr2.append(i)
                if i * i != ssum:              # 제곱수인지 판단
                    arr2.append(ssum // i)
        arr2.sort()         # 순서대로 정렬
        for v in arr2:
            if search(v) and mmax <= v:
                print(n - ssum // v)
                break
