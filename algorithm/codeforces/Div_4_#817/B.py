t = int(input())
for _ in range(t):
    n = int(input())
    up_row = list(map(lambda x: 'G' if x == 'B' else x, input()))
    down_row = list(map(lambda x: 'G' if x == 'B' else x, input()))
    if up_row == down_row:
        print('YES')
    else:
        print('NO')
