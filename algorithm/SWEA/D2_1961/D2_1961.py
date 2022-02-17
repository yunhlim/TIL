def rotate(lst):    # 90도 회전하는 함수
    lst_r = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            lst_r[i][j] = lst[N - 1 - j][i]
    return lst_r


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_r = [0, 0, 0]   # 각각의 배열을 담을 배열 선언
    arr_r[0] = rotate(arr)  # 90도 회전
    arr_r[1] = rotate(arr_r[0]) # 90 + 90 = 180도 회전
    arr_r[2] = rotate(arr_r[1]) # 180 + 90 = 270도 회전
    print(f'#{tc}')

    for i in range(N):
        for j in range(3):  # 각각의 배열의 열들을 순서대로 출력한다.
            print(''.join(map(str, arr_r[j][i])), end=' ')
        print()
