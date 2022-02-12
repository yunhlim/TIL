# SWEA 6318. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 11

SWEA 6318. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 11



**문제 : 다음의 결과와 같이 'abcdef' 문자열의 각각의 문자를 키로 하고 0~5 사이의 정수를 값으로 하는 딕셔너리 객체를 생성하고, 이 딕셔너리 객체의 키와 값 정보를 출력하는 프로그램을 작성하십시오.**

```
Input
없음

Output
a: 0
b: 1
c: 2
d: 3
e: 4
f: 5
```

---

`zip()` 함수를 사용해서 string과 range()의 같은 **index**끼리 묶어주고 이를 `dict()`로 묶어 각각 key와 value로 만들어 준다. `dict()`는 딕셔너리로 만들어주는 함수이다.
딕셔너리는 for 문에서 key값을 순회시켜 사용 가능하다. 이때 값을 사용하고 싶으면 **딕셔너리[key]**를 사용한다.

```python
input_string = 'abcdef'
dic = dict(zip(input_string, range(6)))

for key in dic:   # 딕셔너리 for문 응용
    print(f'{key}: {dic[key]}')
```

결과: **Pass**