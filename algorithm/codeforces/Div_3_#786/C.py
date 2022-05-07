t = int(input())
for _ in range(t):
    s = input()
    t = input()
    if 'a' in t:
        if len(t) == 1:
            print(1)
        else:
            print(-1)
    else:
        print(2 ** (len(s)))