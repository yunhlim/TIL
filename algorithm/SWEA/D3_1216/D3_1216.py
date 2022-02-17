for _ in range(10):
    tc = int(input())
    arr = [input() for _ in range(100)]     # 입력받은 2차원 배열

    arr_t = [[0]*100 for _ in range(100)]   # 2차원 배열을 전치
    for i in range(100):
        for j in range(100):
            arr_t[i][j] = arr[j][i]

    def pallindrome():
        for m in range(100,0,-1):   # m은 회문의 길이
            # row의 회문 탐색
            for i in range(100):
                for j in range(100-m+1):
                    if arr[i][j:j+m] == arr[i][j:j+m][::-1]:
                        print(f'#{tc} {m}')
                        return
                    elif arr_t[i][j:j + m] == arr_t[i][j:j + m][::-1]:
                        print(f'#{tc} {m}')
                        return

    pallindrome()