def recur(prv, visited):
    global ans
    if visited + 1 == 1 << n:           # 다 방문했는지 확인
        return arr[prv][0] or INF   # 도착점까지 이동한 값을 반환(갈 수 없다면 INF 반환)

    if dp[visited][prv] != -1:          # 반복계산을 줄이기 위한 메모이제이션 활용
        return dp[visited][prv]

    ret = INF
    for i in range(1, n):           # 첫번째 비트는 출발점으로 확인할 필요가 없다. 나머지 비트 확인
        if arr[prv][i] == 0 or visited & (1 << i):  # 갈수 없는지, 방문했던 비트인지 확인한다.
            continue
        # 최소값을 리턴, 다음 방문하기 위해 bit를 방문지점에 더해준다.
        ret = min(ret, arr[prv][i] + recur(i, visited | (1 << i)))
    dp[visited][prv] = ret          # 메모이제이션에 값을 넣어준다.
    return ret


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(1 << n)]  # 최소값을 담아 줄 메모이제이션
INF = n * 1000000
print(recur(0, 1))