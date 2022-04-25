n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()      # A의 위치로 오름차순 정렬
for i in range(n):      # B의 위치만 담아준다.
    arr[i] = arr[i][1]
dp = [1 for _ in range(n)]      # LIS 구하기 위한 DP 배열
result = 0              # LIS 길이를 담을 변수
for i in range(n):      # LIS 구하기
    for j in range(i):
        if arr[j] < arr[i]:     # 현재 값보다 작은 값을 찾는다.
            dp[i] = max(dp[i], dp[j] + 1)   # 작은 값 중 현재 길이가 가장 긴 값 + 1과 비교한다.
    result = max(result, dp[i])     # 최댓값 갱신

print(n - result)       # n - LIS