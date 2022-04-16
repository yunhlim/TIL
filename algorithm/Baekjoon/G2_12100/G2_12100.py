def recur(cur):
    global arr, max_result
    if cur == 5:    # 5번 기울인 후 확인
        max_result = max(check(), max_result)
        return
    arr_origin = [arr[i][:] for i in range(n)]      # 원본 값 저장
    move()                                          # 기울이기
    recur(cur + 1)
    for _ in range(3):
        arr = [arr_origin[i][:] for i in range(n)]      # 기울이기 전으로 되돌린다.
        turn()                                          # 90도 회전
        arr_origin = [arr[i][:] for i in range(n)]      # 원본 값 저장
        move()                                          # 기울이기
        recur(cur + 1)


def turn():     # 시계 방향으로 90도 배열을 돌린다.
    arr_origin = [arr[i][:] for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = arr_origin[n-j-1][i]


def move():     # 왼쪽으로 기울인다.
    for i in range(n):
        blocks = []     # 행 별로 블록들을 합쳐준다.
        sum_flag = 0    # 합친 블록인지 표시
        for j in range(n):  # 왼쪽부터 블록들을 확인한다.
            block = arr[i][j]
            if not block:   # 비어있는 경우
                continue
            # 이전 블록을 합치지 않고, 이전 블록 값과 같은 경우
            if sum_flag == 0 and blocks and blocks[-1] == block:
                blocks[-1] = block * 2
                sum_flag = 1    # 합친 블록이라고 표시
            else:
                sum_flag = 0    # 새로 넣어주니 합치지 않았다고 표시
                blocks.append(block)    # 새로 넣어준다.
        blocks += [0] * (n - len(blocks))
        arr[i] = blocks[:]


def check():    # 최댓값을 확인해 현재 최대값보다 큰지 확인한다.
    mmax = 0
    for i in range(n):
        for j in range(n):
            mmax = max(mmax, arr[i][j])
    return mmax


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_result = 0
recur(0)
print(max_result)