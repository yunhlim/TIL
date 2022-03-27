def check(x):   # 매개변수 탐색, x가 가능한지 확인
    total = 0
    for i in range(n):
        if total > x:
            return False
        total += arr[i]
        if total == x:
            total = 0
    return True


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    mmax = 0
    total = 0
    zero_cnt = 0

    for i in range(n):      # 최댓값, 최솟값 구하기
        if mmax < arr[i]:
            mmax = arr[i]
        if arr[i] == 0:
            zero_cnt += 1
        total += arr[i]

    ans = 0
    for i in range(max(1, mmax), total + 1):    # 최댓값 이상부터 가능하니 그 때부터 체크
        if total % i == 0 and check(i):         # 나누어떨어지면 그 수로 가능한지 확인
                ans = n - total // i
                break
    print(ans)