from collections import deque


def calc(num, num2, oper):      # 하나의 연산자를 이용한 계산 하나
    if oper == 1:      # 덧셈
        num += num2
    elif oper == 2:    # 뺄셈
        num -= num2
    elif oper == 3:    # 곱셈
        num *= num2
    else:               # 나눗셈
        if num2 == 0:   # 나눌 수 없는 경우
            return -1
        num //= num2
    if 0 <= num < 1000:     # 세자리까지 가능(음수 X)
        return num
    else:                   # 범위를 넘어서는 경우
        return -1


def recur(cur, x):     # 숫자버튼으로 만들 수 있는 수(세 자리 이하)
    if cur == 3:
        return
    for num in num_keys:
        nxt_num = x * 10 + num
        if visited[nxt_num] <= cur + 1:      # 0으로 시작하는 경우를 처리!
            continue
        visited[nxt_num] = cur + 1      # 클릭 횟수를 배열에 담는다.
        que.append(nxt_num)             # 큐에 담는다.
        nums.append(nxt_num)            # 숫자들을 담아준다.
        recur(cur + 1, nxt_num)


t = int(input())
for tc in range(1, t + 1):
    n, o, m = map(int, input().split())     # n: 터치가능한 숫자들의 개수, o: 터치가능한 연산자들의 개수, m: 최대 터치 횟수
    num_keys = list(map(int, input().split()))      # 사용 가능한 숫자들 0 ~ 9
    opers = list(map(int, input().split())) # 사용 가능한 연산자들 +는 1, -는 2, *은 3, /는 4
    nums = []
    w = int(input())        # 원하는 출력 값
    INF = m + 1             # m은 최대 20이니 더 큰 값을 넣어준다.
    visited = [INF for _ in range(1000)]
    que = deque()
    recur(0, 0)     # 숫자로만 구성할 수 있는 세자리 이하 수들을 담아준다.

    if visited[w] < INF:     # 숫자로만 구성할 수 있으면 출력하고 종료
        print(f'#{tc} {visited[w]}')
        continue

    while que:
        v = que.popleft()
        for num in nums:
            click_cnt = visited[v] + len(str(num)) + 1
            if click_cnt + 1 > m:           # 클릭 횟수가 m을 초과한 경우('='하나 포함)
                continue
            for oper in opers:
                nxt = calc(v, num, oper)
                if nxt == -1:           # 예외사항 처리
                    continue
                if visited[nxt] <= click_cnt:   # 클릭 횟수가 같거나 커지면 패스
                    continue
                visited[nxt] = click_cnt        # 클릭 횟수가 더 작으면 업데이트
                que.append(nxt)

    if visited[w] < INF:     # 숫자로만 구성할 수 있으면 출력하고 종료
        print(f'#{tc} {visited[w] + 1}')    # '='도 누르는 횟수 포함
    else:
        print(f'#{tc} -1')