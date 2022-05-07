t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if y // x != y / x:
        print(0, 0)
    else:
        print(1, y // x)