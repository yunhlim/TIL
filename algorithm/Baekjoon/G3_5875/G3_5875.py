arr = [0] + [1 if x == '(' else -1 for x in input()]      # 괄호가 '('이면 1, ')'이면 -1
prefix_sum = [0 for _ in range(len(arr))]       # 괄호의 누적합

for i in range(1, len(arr)):                    # 괄호의 누적합을 구한다.
    prefix_sum[i] = arr[i] + prefix_sum[i - 1]

cnt = 0
if prefix_sum[-1] == 2:      # 여는 괄호가 더 많을 때
    for i in range(1, len(arr))[::-1]:
        if prefix_sum[i] == 1:  # 현재 인덱스의 누적합이 1이면 종료
            break               # 바꾸면 음수가 되므로 불가능
        if arr[i] == 1:     # 여는 괄호를 닫는 괄호로 바꿀 수 있다.
            cnt += 1
elif prefix_sum[-1] == -2:                       # 닫는 괄호가 더 많을 때
    for i in range(1, len(arr)):    # 음수가 나오면 그 수까지 확인하고 종료
        if arr[i] == -1:
            cnt += 1
        if prefix_sum[i] < 0:   # 현재 인덱스의 누적합이 음수가 처음 나왔다면 이 괄호까지만 변경 가능
            break               # 다음 인덱스부터 바꾸면 음수가 있는 인덱스가 존재해버린다.
print(cnt)