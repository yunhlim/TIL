# [Programmers] Lv 2. k진수에서 소수 개수 구하기 [2022 KAKAO BLIND RECRUITMENT]

## 📚 문제 : [k진수에서 소수 개수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/92335)

## 📖 풀이

주어진 수를 k진수로 바꾼 후 0으로 구분된 숫자들이 소수인지 판별하는 문제이다.

1. 소수 판별
   - 소수를 판별하는 함수를 하나 만든다. 
   - **제곱근 이하**만 보는 규칙을 활용해 시간복잡도를 줄인다.

2. k로 나누며 소수 개수 판별

- k로 나누면서 나머지 값을 string에 따로 저장한다. string으로 저장하며 나머지를 왼쪽에 붙여나간다.
- n이 0이 되어 더 이상 나눌 수 없으면 저장한 string이 소수인지 판별하고 종료한다.

- n을 k로 나눈 나머지가 0이면 string이 소수인지 판별하고 string을 0으로 만든다. 그리고 n을 n // k로 바꾼다.

- n을 k로 나눈 나머지가 0이 아니면 string 왼쪽에 n % k를 붙이고, n은 n // k로 바꾼다.

위 규칙을 반복한다.

## 📒 코드

```python
def solution(n, k):
    def check(x):       # 소수인지 체크
        nonlocal cnt
        for i in range(2, x + 1):
            if i * i > x:       # 제곱근 이하만 본다.
                cnt += 1        # 나누어 떨어지는 수가 없으니 + 1
                return
            if not x % i:       # 1이 아닌 수로 나누어 떨어지면 return
                return
        else:
            return
    
    
    def recur(n, p_str):    # n은 현재 수, p_str은 0 사이의 수(int가 아니라 str)
        if n == 0:          # n이 0이면 p_str를 체크하고 종료
            if p_str:
                check(int(p_str))
            return
        if n % k:           # n이 k로 나누어 떨어지지 않으면
            p_str = str(n % k) + p_str     # p_str에 나머지를 왼쪽에 붙인다.
        else:               # 나누어 떨어지면
            if p_str:       # 소수인지 체크
                check(int(p_str))
            p_str = ""      # p_str 초기화
        n //= k             # 나눈 몫으로 n을 초기화
        recur(n, p_str)     # n이 0이 될 때까지 반복
        
        
    cnt = 0
    recur(n, "")
    
    return cnt
```

