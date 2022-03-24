# [SWEA] 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 [D2]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDLaK1kMDFAVT#

---

## 📖 풀이

입력받은 수를 실수계산하지 않고 정수로 바꿔 계산해본다.

12자리까지 확인하고 넘어가면 overflow를 출력하니 입력받은 소수의 소수점 자리만 12자리의 정수로 바꿔준다.

0.625를 입력받으면 625000000000로 적어준다.

그리고 10 ** 12 를 2로 나누면서 입력받은 수보다 작으면 빼준다.

뺄 수 있으면 빼고 출력할 값에 1을붙이고 뺄 수 없으면 0을 붙인다.

## 📒 코드

```python
def binary(n):
    n = n[2:]
    value = 10 ** 12                    # 주어진 입력에서 뺄 정수
    n = int(n) * 10 ** (12 - len(n))    # 입력된 소수를 12자리 정수로 바꾼다.
    ans = ''
    cnt = 0     # 12번까지 가능
    while n != 0 and cnt < 12:
        cnt += 1
        value //= 2
        if value <= n:          # 뺄 수 있으면 뺀 후 1을 붙인다.
            n -= value
            ans += '1'
        else:                   # 뺄 수 없으면 0을 붙인다.
            ans += '0'
    if n != 0:                  # 0이 안된 경우 overflow 출력
        return 'overflow'
    return ans


for tc in range(1, 1 + int(input())):
    n = input()
    print(f'#{tc} {binary(n)}')
```

## 🔍 결과

![image-20220324203951588](README.assets/image-20220324203951588.png)