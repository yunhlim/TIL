# [Algorithm] 소인수 분해 (정수론)

## 📒 완전 탐색 코드 - 시간초과

```python
n = int(input())
for i in range(2, n+1):
    while n % i == 0:
        print(i)
        n //= i
```



## 📖 시간 초과를 줄이는 방법

소인수가 n의 제곱근보다 큰 경우는 1개이거나 없다. 

따라서 제곱근 이하인 경우만 확인하고, 남은 x가 1보다 크면 그걸 출력하고 종료한다.

```python
n = int(input())

x = n

for i in range(2, n + 1):
    if i * i > n:
        break
        
    while x % i == 0:	# 여러 개의 소수의 곱이 포함될 수 있으니 계속 나누어주며 출력한다.
        print(i)
        x //= i
if x != 1:				# 제곱근보다 큰 경우가 있다면 출력한다.
    print(x)
```

