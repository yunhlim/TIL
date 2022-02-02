N = int(input())
nums = list(map(int,input().split()))
cnt = 0
for num in nums:
    if num == 1:    # 1은 소수가 아니다!
        continue
    else: 
        for i in range(2, num): # 2부터 num-1까지의 수 중 하나라도 나누어 떨어지면 소수가 아니다.
            if num % i == 0:
                break
        else: cnt += 1  # 위에서 안 나누어 떨어지면 소수
print(cnt)