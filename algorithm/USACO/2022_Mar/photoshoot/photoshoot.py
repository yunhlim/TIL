n = int(input())
arr = input()

prv = -1    # 이전 조합 기억
cnt = 0     # 회전하는 횟수
for i in range(0, n, 2):    # 2개 씩 확인
    if arr[i] == arr[i + 1] or prv == arr[i]:   # 2개가 같거나 이전에 나왔던 조합과 같으면 continue
        continue
    prv = arr[i]    # 다른 조합이 나오면 이전 값에 적어주고
    cnt += 1        # 회전 + 1

if prv == 'H':      # 이미 짝수가 가장 많은데 홀수가 가장 많게 뒤집어 버린 경우 -1 해준다.
    cnt -= 1
print(cnt)