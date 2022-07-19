a, b, v = map(int, input().split())
v -= a
print(1 + v // (a - b) + (1 if v % (a - b) else 0))