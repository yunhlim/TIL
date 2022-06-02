def one_calc(num, num2, oper):
    num = 0
    if oper == 11:      # 덧셈
        num += num2
    elif oper == 12:    # 뺄셈
        num -= num2
    elif oper == 13:    # 곱셈
        num *= num2
    else:               # 나눗셈
        num //= num2
    return num


def many_calc(f):
    result = 0
    oper = 0
    num = 0
    for btn in f:
        if btn > 10:  # 연산자인 경우
            if oper > 0:        # 연산자가 2번 나온 경우부터 계산
                result = one_calc(result, num, oper)
            num = 0
            oper = btn
        if btn < 10:    # 숫자인 경우
            num = num * 10 + btn
    if oper > 0:
        result = one_calc

    if 0 <= result < 999:
        return result
    else:
        return -1       # 잘못된 경우


# t = int(input())
# for tc in range(1, t + 1):
#     n, o, m = map(int, input().split())     # n: 터치가능한 숫자들의 개수, o: 터치가능한 연산자들의 개수, m: 최대 터치 횟수
#     nums = list(map(int, input().split()))
#     opers = list(map(lambda x: int(x) + 10, input().split())) # +는 1, -는 2, *은 3, /는 4
#     w = int(input())
#     dp = [[] for _ in range(m)]

#     for num in nums:        # 한 번 누른 경우 담기(숫자들만)
#         dp[0].append(num)

#     for i in range(1, m):
#         for j in dp[i-1]:

print(calc([10,11,2]))