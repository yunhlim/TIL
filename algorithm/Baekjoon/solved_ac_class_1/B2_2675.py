import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, string = input().split()
    n = int(n)
    result = ''
    for c in string:
        result += c * n
    print(result)