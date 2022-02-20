T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    coin = 0
    for i in range(N):
        for j in range(abs(i - N//2), N - abs(i - N//2)):
            coin += arr[i][j]
    print(f'#{tc} {coin}')