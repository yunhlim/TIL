def recur(x, y):

    while arr[x][y] == 0:   # 
        if x == 5:
            x = 0
            y += 1
        if y == 5:
            return
    
    

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]