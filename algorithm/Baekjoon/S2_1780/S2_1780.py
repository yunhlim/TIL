def recur(x, y, size):
    start = arr[x][y]
    same = False
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != start:
                break


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
