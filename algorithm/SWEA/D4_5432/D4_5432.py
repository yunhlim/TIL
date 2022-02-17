# 쇠막대기 자르기
T = int(input())
for tc in range(1, T + 1):
    gwalho = ' ' + input()
    cnt = 0
    result = 0
    for i in range(1, len(gwalho)):
        if gwalho[i] == '(':   # cnt 1 증가
            cnt += 1
        else:
            cnt -= 1
            if gwalho[i-1] == '(':
                result += cnt
            else: result += 1
    print(f'#{tc} {result}')
