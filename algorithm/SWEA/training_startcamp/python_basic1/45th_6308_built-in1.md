# SWEA 6308. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 1

SWEA 6308. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 1



**문제 : 다음의 결과와 같이 이름과 나이를 입력 받아 올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.**

```
Input
홍길동
20

Output
홍길동(은)는 2099년에 100세가 될 것입니다.
```

---

왜 내장함수 문제인지는 모르겠지만 간단히 풀었다...

```python
name = input()
age = int(input())

print(f'{name}(은)는 {age+2079}년에 100세가 될 것입니다.')
```

결과 : **Pass**