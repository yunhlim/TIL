def binary(n):
    n = n[2:]
    value = 10 ** 12                    # 주어진 입력에서 뺄 정수
    n = int(n) * 10 ** (12 - len(n))    # 입력된 소수를 12자리 정수로 바꾼다.
    ans = ''
    cnt = 0     # 12번까지 가능
    while n != 0 and cnt < 12:
        cnt += 1
        value //= 2
        if value <= n:          # 뺄 수 있으면 뺀 후 1을 붙인다.
            n -= value
            ans += '1'
        else:                   # 뺄 수 없으면 0을 붙인다.
            ans += '0'
    if n != 0:                  # 0이 안된 경우 overflow 출력
        return 'overflow'
    return ans


for tc in range(1, 1 + int(input())):
    n = input()
    print(f'#{tc} {binary(n)}')