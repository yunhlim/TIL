N, K = map(int, input().split())

if N-K < K:
    K = N-K

up_nums = 1
down_nums = 1

for i in range(N,N-K,-1):
    up_nums *= i

for i in range(1,K+1):
    down_nums *= i

print(up_nums//down_nums)
