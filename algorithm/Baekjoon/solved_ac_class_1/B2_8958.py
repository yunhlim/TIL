t = int(input())
for _ in range(t):
    arr = list(input())
    cnt = 0
    result = 0
    for ox in arr:
        if ox == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)