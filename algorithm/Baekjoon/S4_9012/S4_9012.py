def check():
    stack = []
    for x in ps:
        if x == '(':    # 열린 괄호는 스택에 넣는다.
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:       # stack에 없는데 꺼내려고 하면 VPS가 아니다.
                return 'NO'
    if stack:
        return 'NO'
    else:
        return 'YES'

n = int(input())
for _ in range(n):
    ps = input()        # 입력으로 받은 괄호 문자열
    print(check())