def recur(x, y):
    if x == 1 or y == 1:
        return x + y - 2
    if x <= y:
        a = y // 2
        b = y - a
        return recur(x, a) + recur(x, b) + 1
    else:
        a = x // 2
        b = x - a
        return recur(a, y) + recur(b, y) + 1
        

n, m = map(int, input().split())
print(recur(n, m))