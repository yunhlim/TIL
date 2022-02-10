# N = int(input())
# nums = list(map(int,input().split()))
# cnt = 0
# for num in nums:
#     if num == 1:    # 1은 소수가 아니다!
#         continue
#     else: 
#         for i in range(2, num): # 2부터 num-1까지의 수 중 하나라도 나누어 떨어지면 소수가 아니다.
#             if num % i == 0:
#                 break
#         else: cnt += 1  # 위에서 안 나누어 떨어지면 소수
# print(cnt)



# 제곱근 활용해서 더 효율적으로 구하기
N = int(input())
nums = list(map(int,input().split()))
sosu_cnt = 0    # 소수 cnt
for num in nums:
    cnt = 0     # 1이 아닌 약수가 있는지 센다.
    if num == 1:    # 1은 소수 X
        continue
    for i in range(2, num):
        if i * i > num: # 제곱근보다 작거나 같을 때만 약수가 나온다.
            break
        if num % i == 0:
            cnt += 1    # 나누어 떨어지면 약수를 더한다.
    if cnt == 0: sosu_cnt += 1    # 약수가 없으면 소수 cnt 증가
print(sosu_cnt)