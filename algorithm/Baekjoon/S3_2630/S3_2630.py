def is_color(y1, y2, x1, x2):   # 색이 다 같은지 확인
    color = arr[y1][x1]
    for i in range(y1, y2):
        for j in range(x1, x2):
            if arr[i][j] != color:  # 다르면 False
                return False
    return True                     # 같으면 True


def b_search(y1, y2, x1, x2):   # 색종이 이진 탐색
    global ones, zeros
    if is_color(y1, y2, x1, x2):    # 색이 같으면 무슨 색인지 찾아서 cnt를 증가
        if arr[y1][x1]:       # 1이 있으니 ones 증가
            ones += 1
        else:                 # 0이 있으니 zeros 증가
            zeros += 1
        return                # 구간의 색이 다 같은 색종이는 stop
    else:                     # 색종이의 색이 다르면 4 구간으로 분할
        b_search(y1, y1 + (y2-y1)//2, x1, x1 + (x2-x1)//2)
        b_search(y1, y1 + (y2-y1)//2, x1 + (x2-x1)//2, x2)
        b_search(y1 + (y2-y1)//2, y2, x1, x1 + (x2-x1)//2)
        b_search(y1 + (y2-y1)//2, y2, x1 + (x2-x1)//2, x2)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
zeros = 0
ones = 0
b_search(0, N, 0, N)
print(zeros)
print(ones)