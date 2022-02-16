A, B = map(int, input().split())
b = B # B 이하의 2의 거듭제곱이 존재하는 영역까지 구하기 위해 나누어줄 B 값
exp = 0         # 2의 지수
sum = B-A+1     # 먼저 전 영역에 1을 다 더해준다.
while b >= 2:   # 더 이상 2의 배수가 없을 때까지
    b //= 2     # B보다 작은 2의 거듭제곱으로 나누어주기 위해 계속 나누며 확인한다.
    exp += 1    # 2의 지수를 1 더한다.
    two_exp = 2**exp    # 2의 거듭제곱 값
    sum += (B//two_exp - (A-1)//two_exp) * (two_exp//2) # [A, B] 영역에서 배수의 개수에 2의 거듭제곱의 절반을 곱한다.
print(sum)