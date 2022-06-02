def calc(num, num2, oper):      # 하나의 연산자를 이용한 계산 하나
    if oper == 11:      # 덧셈
        num += num2
    elif oper == 12:    # 뺄셈
        num -= num2
    elif oper == 13:    # 곱셈
        num *= num2
    else:               # 나눗셈
        if num2 == 0:   # 나눌 수 없는 경우
            return -1
        num //= num2
    return num


def recur(cur, x):     # 숫자버튼으로 만들 수 있는 수(세 자리 이하)
    if cur == 3:
        return
    for num in nums:
        visited[x * 10 + num] = cur + 1
        recur(cur + 1, x * 10 + num)


t = int(input())
for tc in range(1, t + 1):
    n, o, m = map(int, input().split())     # n: 터치가능한 숫자들의 개수, o: 터치가능한 연산자들의 개수, m: 최대 터치 횟수
    nums = list(map(int, input().split()))      # 사용 가능한 숫자들 0 ~ 9
    opers = list(map(lambda x: int(x) + 10, input().split())) # 사용 가능한 연산자들 +는 11, -는 12, *은 13, /는 14
    w = int(input())        # 원하는 출력 값
    visited = [0 for _ in range(1000)]
    recur(3, 0)
    print(f'#{tc} {recur(0)}')