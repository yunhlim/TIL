import sys

n = int(input())
s1 = set()
for _ in range(n):
    x = tuple(sys.stdin.readline().split())
    if len(x) == 2:
        if x[0] == 'add':
            s1.add(int(x[1]))
        elif x[0] == 'remove':
            s1.discard(int(x[1]))
        elif x[0] == 'check':
            if int(x[1]) in s1:
                print(1)
            else:
                print(0)
        else:
            if int(x[1]) in s1:
                s1.discard(int(x[1]))
            else:
                s1.add(int(x[1]))
    else:
        if x[0] == 'all':
            s1 = set(range(1, 21))
        else:
            s1 = set()