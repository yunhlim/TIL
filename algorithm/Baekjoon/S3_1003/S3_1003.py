memo = [[0, 0] for _ in range(41)]
memo[0] = [1, 0]
memo[1] = [0, 1]
cnt = 1
for i in range(int(input())):
    n = int(input())
    while cnt < n:
        for i in range(2):
            memo[cnt + 1][i] = memo[cnt][i] + memo[cnt - 1][i]
        cnt += 1
    
    print(*memo[n])