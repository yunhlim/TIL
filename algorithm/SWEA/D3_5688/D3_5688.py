t = int(input())
for tc in range(1, 1 + t):
    n = int(input())
    result = -1
    for i in range(1, n + 1):
        if i * i * i > n:  # 세제곱근보다 커지면 종료
            break

        if i * i * i == n:  # 같은 값이 있는지 확인
            result = i
            break

    print(f'#{tc} {result}')