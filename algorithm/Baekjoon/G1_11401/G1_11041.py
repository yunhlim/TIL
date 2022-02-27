N, K = map(int, input().split())
M = 1_000_000_007
result = 1

for i in range(N-K+1, N+1):         # N! / (N-K)!의 mod 구하기
    result = (result * (i % M)) % M
result1 = 1
for i in range(1, K+1):             # K!의 mod 값 구하기
    result1 = (result1 * (i % M)) % M

# 1/K!의 mod 값은 (K!)^(M-2)의 mod 값이랑 같다.
# 분할정복으로 n의 m 거듭제곱 값 구하기
def pows(n,m):                      
   
    if m == 0:
        return 1
    
    ret = pows(n,m//2)      # 재귀를 활용하여 거듭제곱의 연산과정을 줄인다.
    ret *= ret
    ret %= M                # 나머지 값만 구하면 되니 연산 과정마다 나누어 준다.

    if m % 2 == 0:
        return ret
    else:
        return (ret * n) % M

print((result * pows(result1, M-2)) % M)