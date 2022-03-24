def search(n, m):
    for i in range(n):
        if m % 2 == 0:
            return 'OFF'
        m //= 2
    return 'ON'


for tc in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    print(f'#{tc} {search(n, m)}')