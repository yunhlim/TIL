# [SWEA] 10726. 이진수 표현 [D3]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXRSXf_a9qsDFAXS&categoryId=AXRSXf_a9qsDFAXS&categoryType=CODE&problemTitle=%EC%9D%B4%EC%A7%84%EC%88%98+%ED%91%9C%ED%98%84&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

## 📖 풀이

이진수가 주어지면 마지막 N 비트가 모두 1인지 확인하는 문제이다.

마지막 N비트는 자릿수가 작은 비트다.

따라서 n번 2로 나눠가며 나머지가 0이 나오면 OFF를 출력하고 아니면 ON을 출력한다.

## 📒 코드

```python
def search(n, m):
    for i in range(n):
        if m % 2 == 0:
            return 'OFF'
        m //= 2
    return 'ON'


for tc in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    print(f'#{tc} {search(n, m)}')
```

## 🔍 결과

![image-20220324205056854](README.assets/image-20220324205056854.png)