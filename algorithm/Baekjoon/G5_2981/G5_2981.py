def gcd(big, small):    # 최대 공약수
    while big % small:
        big, small = small, big % small
    return small

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()                          # 수를 정렬
for i in range(1, N):               # 젤 작은 수로 나머지 수를 빼서 arr에 담는다.
    arr[i] = arr[i] - arr[0]
del arr[0]                          # 젤 작은 수를 제거, 서로 뺀 차이만 남긴다.
                                # 위 배열에 있는 수들의 공약수를 구하면 된다.
num = arr[0]                    # 최대 공약수를 담을 변수, 첫 번째 수를 담는다.
for i in range(1, len(arr)):    # 최대 공약수와 수들을 하나씩 다시 최대 공약수를 구해준다.
    num = gcd(num, arr[i])

result = []                     # 약수를 담을 배열
for i in range(1, num + 1):     # 최대 공약수의 약수들을 구해 공약수들을 찾아준다.
    if i * i >= num:
        if i * i == num:
            result += [i]
        break
    if num % i == 0:
        result += [i, num // i]
result.sort()                   # 최대 공약수들을 다시 정렬

del result[0]                   # 1은 뺀다.
print(*result)