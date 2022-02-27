# [Baekjoon] 11402. 이항 계수 4 [P4]

## 📚 문제

https://www.acmicpc.net/problem/11402

---

N과 K가 클 땐 팩토리얼 계산을 할 때 시간초과가 발생한다. 따라서 N과 K가 클 땐 뤼카의 정리를 이용한다.

**뤼카의 정리**로 이항 계수의 두 수를 줄여준다.

뤼카의 정리를 간단히 설명하면 다음과 같다.

>nCm mod 7일 경우
>
>n과 m을 7진법으로 나타낸다.
>
>n = `a*7^2 + b*7^1 + c`
>
>m = `d*7^2 + e*7^1 + f`
>
>nCm mod 7 = `aCd * bCe * cCf mod 7`가 된다.

nCm을 M보다 작은 n과 m으로 이루어진 여러개의 이항 계수로 나누어준다.

나누기 위해 입력으로 받은 N과 K를 M진법으로 나타내야 한다.

M으로 나눈 나머지와 몫을 이용해 M진법으로 나타내어 준다. 이 때 함수를 만들어서 처리한다.

이항 계수를 계산해주는데 이 때 모듈러의 성질을 이용해 계속 값을 M으로 나눈 나머지로 바꿔준다.

그리고 페르마의 소정리를 이용하기 위한 거듭제곱은 분할정복을 활용하여 계산해준다. 이때에도 거듭제곱을 해주는 함수를 따로 만들어준다.

## 📒 코드

```python
def jinsu(n, m):    # n을 n진법으로 변환
    arr = []
    while True:
        if n < m:           # m진법으로 나타내다가 최고자리 값 나오면 마지막에 붙인다.
            arr.append(n)
            break
        arr.append(n % m)   # M진법을 오른쪽부터 적는게 아니라 계산하기 편하게 왼쪽부터 적는다.
                            # 모듈러의 성질을 이용하게 M으로 나눈 나머지를 넣는다.
        n //= m
    return arr

def pows(n, p):     # n을 p의 거듭제곱을 분할정복으로 구한다.
    if p == 0:
        return 1
    else:
        x = pows(n, p // 2)
        x *= x
        x %= M          # 모듈러의 성질 이용
        if p % 2:
            return (x * n) % M  # 모듈러의 성질을 이용하기 위해 M으로 나눈 나머지로 변환
        else:
            return x

N, K, M = map(int,input().split())

if N - K < K:       # nCn-k = nCk를 응용해서 식을 줄인다.
    K = N - K

n_arr = jinsu(N, M)     # 뤼카의 정리를 이용하기 위해 N과 K를 M진법으로 나타낸다.
k_arr = jinsu(K, M)
k_arr = k_arr + [0] * (len(n_arr) - len(k_arr))     # K의 상위자리를 0으로 채운다.


result = 1          # 나오는 값에 곱해줄 결과 값

for i in range(len(n_arr)): # M진법의 각 자리수 별로 nCm % M 연산을 해주고 곱한다.
    n = n_arr[i]    # N의 M진법으로 나타낸 각 자리 수
    m = k_arr[i]    # K를 M진법으로 나타낸 각 자리 수

    if n < m:       # n보다 m이 더 크면 뤼카의 정리는 무조건 0이 나온다.
        result = 0
        break

    for i in range(n-m+1, n+1):
        result *= i
        result %= M         # 모듈러의 성질 이용
    
    temp = 1
    for i in range(1, m+1):
        temp *= i
        temp %= M           # 모듈러의 성질 이용

    result *= pows(temp, M-2)   # 페르마의 소정리를 이용해 1/K! mod M => K!^(M-2) mod M으로 변경
    result %= M             # 모듈러의 성질 이용

print(result)
```

## 🔍 결과

![image-20220227232347571](README.assets/image-20220227232347571.png)