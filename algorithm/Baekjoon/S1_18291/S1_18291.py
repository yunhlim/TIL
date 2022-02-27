T = int(input())

def pows(n, p):     # 분할정복을 활용한 n의 p 거듭제곱 값 구하기
    if p == 0:
        return 1
    else:
        x = pows(n, p // 2)
        x *= x
        x %= 1000000007     # 10^9 + 7로 나눈 값을 구해야하므로 모듈러의 성질을 이용해 연산과정마다 계산한다.
        if p % 2:
            return (x * n) % 1000000007
        else:
            return x

for _ in range(T):
    N = int(input())
    if N > 2:
        print(pows(2, N-2))
    else:           # N이 2이하일 때는 1이다.
        print(1)