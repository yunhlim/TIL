def binary_to_decimal():    # 2진수를 10진수로 변경(string => int)
    cnt = 1
    decimal = 0
    for c in two[::-1]:
        decimal += cnt * c
        cnt *= 2
    return decimal


def decimal_to_ternary(decimal):    # 10진수를 3진수 변경(int => string)
    result = ''
    while decimal >= 3:
        result = str(decimal % 3) + result
        decimal //= 3
    if decimal:
        result = str(decimal) + result
    return result


def func():
    for i in range(len(two)):
        two[i] = two[i] ^ 1                 # 2진수를 한 자리씩 변경
        decimal = binary_to_decimal()       # 2진수를 10진수로 변경
        ans = decimal_to_ternary(decimal)   # 10진수을 3진수으로 변경
        if len(ans) == len(three):          # 서로 길이가 같은 지 확인
            cnt = 0
            for j in range(len(three)):     # 다른 개수가 하나인지 확인
                if cnt == 2:                # 다른 개수가 2이상이면 break
                    break
                if ans[j] != three[j]:
                    cnt += 1
            else:                           # 다른 개수가 하나일 때 return
                if cnt == 1:
                    return decimal
        two[i] = two[i] ^ 1                 # 바꿔준 자리를 원상복구


for tc in range(1, 1 + int(input())):
    two = list(map(int, input()))
    three = input()
    print(f'#{tc} {func()}')

