# SWEA 6311. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 4

SWEA 6311. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 4



**문제 : "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.**

```
Input
없음

Output
184
```

---

`map(x,y)` 함수를 사용한다. y라는 자료형의 각각에 x라는 함수를 적용해 바꾸어주는 함수이다.

x라는 함수는 람다식을 활용해 if else 구문을 반복해 만들어준다.

**람다식에 조건문을 넣을 땐 elif를 사용할 수 없고 break도 사용할 수 없다.** 따라서 조건문을 중첩으로 if else를 반복해 만들어야 한다.

```python
text = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
total = 0

scores = list(map(lambda x: 4 if x=='A' else 3 
if x=='B' else 2 if x=='C' else 1, text))

for score in scores:
    total += score
    
print(total)
```

결과 : **Pass**