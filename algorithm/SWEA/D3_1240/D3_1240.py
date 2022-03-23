def find_code(x, y):        # 암호 위치를 찾는다.
    if y < 6:               # y 값이 6보다 작아지면 다음 행 탐색
        y = m - 1
        x += 1
    if arr[x][y] != '0':    # 0이 아닌 수가 나오면 암호를 찾은 것이다.
        return x, y - 55   # 암호의 시작점을 반환
    else:
        return find_code(x, y - 1)  # 0이 나오면 다음 열을 탐색


def solve_code(x, y):           # 암호 시작점을 받아 해독한다.
    code = arr[x][y:y + 56]     # 암호의 길이 56
    result = [0]                # 시작부분에 padding을 넣어준다.
    for i in range(8):          # 딕셔너리에 적은 코드와 같으면 그 값인 숫자로 넣어준다.
        result.append(d[code[0 + i * 7:(i + 1) * 7]])
    odd_sum, even_sum = 0, 0
    for i in range(1, 9):
        if i % 2:               # 홀수일 때와 짝수일 때 각각의 합을 찾는다.
            odd_sum += result[i]
        else:
            even_sum += result[i]

    if (odd_sum * 3 + even_sum ) % 10:  # 계산 후 10으로 나누어 떨어지는지 판별
        return 0
    else:
        return sum(result)


d = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,\
'0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    print(f'#{tc} {solve_code(*find_code(0, m - 1))}')