# [Algorithm] 약수 구하기 (정수론)

약수 구하기도 소수 판정과 비슷하다.

완전 탐색으로 하는 경우는 안 된다.

제곱근 이하까지 구하는데 **제곱수**인 경우를 생각해야 한다.

쌍으로 나오는 것들이 같아지니 `if i*i != n:` 넣어주게 한다.

> 약수의 개수가 홀수인 것과 제곱수랑 필요충분조건이다.

## 📒 코드

```python
n = int(input())
prime = []

for i in range(1,n+1):
    if i*i > n:
        break
        
    if n % i = 0:
        prime.append(i)
        if i*i != n: # 제곱수를 막기 위함
        	prime.append(n//i)

prime(*prime)
```

