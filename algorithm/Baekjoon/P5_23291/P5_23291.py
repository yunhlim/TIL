# 어항을 돌린 후 올리기
def turn_stack(cur):
    global arr
    r, c = len(arr), len(arr[0])
    # 홀수 번 회전인 경우
    if not (cur % 2):
        if r * 2 > c:       # 어항의 범위를 넘어서는 경우
            return
    # 짝수 번 회전인 경우
    else:
        if r * 2 - 1 > c:   # 어항의 범위를 넘어서는 경우
            return
    copy_arr = [arr[i][:] for i in range(len(arr))]

    x, y = pick(r, c)   # 회전할 박스 선택
    box = [arr[i][:y][:] for i in range(x)]
    box = turn_90(box, x, y)
    arr = [[0] * (c - y) for _ in range(y + 1)]

    # 첫줄 만들기
    for i in range(c - y):
        arr[-1][i] = copy_arr[-1][y + i]

    # 회전한 박스 쌓기
    for i in range(len(box)):
        for j in range(len(box[0])):
            arr[i][j] = box[i][j]
    turn_stack(cur + 1)


# 반으로 쪼개서 쌓기
def half_stack(cur):
    global arr

    if cur == 2:    # 2번만 시행
        return

    r, c = len(arr), len(arr[0])
    copy_arr = [arr[i][:] for i in range(len(arr))]

    box = [arr[i][:c // 2][:] for i in range(r)]
    # 180도 돌리기
    box = turn_90(box, r, c // 2)
    box = turn_90(box, c // 2, r)
    arr = [[0] * (c // 2) for _ in range(r * 2)]

    for i in range(r):
        for j in range(c // 2):
            # 하단 박스 놓기
            arr[i + r][j] = copy_arr[i][j + c // 2]
            # 회전한 박스 놓기
            arr[i][j] = box[i][j]
    half_stack(cur + 1)


# 현재 회전할 박스 선택
def pick(r, c):
    if r == 1:
        return 1, 1
    else:
        for i in range(c):
            if arr[0][i] == 0:
                return r, i


# 박스 90도 회전
def turn_90(box, x, y):
    turn_box = [[0] * x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            turn_box[i][j] = box[x - j - 1][i]
    return turn_box


# 어항 정리 완료했는지 확인
def check_complete():
    if k >= max(arr[0]) - min(arr[0]):
        return True
    else:
        return False


# 처음에 물고기 채우기
def fill_fish():
    min_cnt = min(arr[0])
    for i in range(len(arr[0])):
        if min_cnt == arr[0][i]:
            arr[0][i] += 1


# 물고기 수 조절
def fish_move():
    global arr
    copy_arr = [arr[i][:] for i in range(len(arr))]
    r, c = len(arr), len(arr[0])
    for x in range(r):
        for y in range(c):
            if arr[x][y] == 0:
                continue
            for k in range(2):  # 오른쪽 아래만 확인
                nx = x + dx[k]
                ny = y + dy[k]
                if not(0 <= nx < r and 0 <= ny < c) or not arr[nx][ny]:
                    continue
                move_fish = abs(copy_arr[x][y] - copy_arr[nx][ny]) // 5
                if copy_arr[x][y] > copy_arr[nx][ny]:
                    arr[x][y] -= move_fish
                    arr[nx][ny] += move_fish
                elif copy_arr[x][y] < copy_arr[nx][ny]:
                    arr[x][y] += move_fish
                    arr[nx][ny] -= move_fish


# 어항을 다시 일렬로
def change_row():
    global arr
    copy_arr = [arr[i][:] for i in range(len(arr))]
    r, c = len(arr), len(arr[0])
    arr = [[]]
    for i in range(c):
        for j in range(r):
            if copy_arr[r - j - 1][i] != 0:
                arr[0].append(copy_arr[r - j - 1][i])


# 어항 정리
def clean():
    fill_fish()
    turn_stack(0)
    fish_move()
    change_row()
    half_stack(0)
    fish_move()
    change_row()


n, k = map(int, input().split())
arr = [list(map(int, input().split()))]
dx, dy = [0, 1], [1, 0]     # 우, 하
cnt = 0
while not check_complete():
    cnt += 1
    clean()

print(cnt)
