def recur(x, y, size):
    start = arr[x][y]
    same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != start:
                same = False
                break

    if same == True:
        result[start] += 1
    else:
        size //= 3
        for i in range(3):
            for j in range(3):
                recur(x + size * i, y + size * j, size)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = {-1: 0, 0: 0, 1: 0}
recur(0, 0, n)
print(result[-1])
print(result[0])
print(result[1])
