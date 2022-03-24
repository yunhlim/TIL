def ten_to_binary(n):           # 10진수를 2진수로 변환
    ans = ''
    for i in range(4):          # 4자리
        ans = str(n % 2) + ans  # 나머지를 왼쪽에 붙여준다.
        n //= 2
    return ans


def hex_to_binary(n):           # 16진수를 2진수로 변환(10진수로 바꾸고 2진수로 바꿔준다)
    ans = ''
    for c in n:                 # 입력받은 16진수 순회
        if c.isdigit():         # 숫자인 경우
            ans += ten_to_binary(int(c))
        else:                   # 문자인 경우 딕셔너리 활용
            ans += ten_to_binary(hex_c[c])
    return ans


hex_c = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for tc in range(1, 1 + int(input())):
    n, num = input().split()
    print(f'#{tc} {hex_to_binary(num)}')