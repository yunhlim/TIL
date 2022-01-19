# SWEA 6316. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 9

SWEA 6316. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 9



**문제 : 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해 짝수만을 선택한 후, map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.**

```
Input
없음

Output
[4, 16, 36, 64, 100]
```

---

`filter()`함수는 `map()`와 비슷한데 map은 전체 인수들을 바꾸어주는 것이라고 하면 filter는 특정 인덱스만 골라 새로운 배열로 만들어는 함수이다.

```python
nums = list(range(1,11))

def evens_double(numbers):
    result = numbers
    result = list(filter(lambda x: x%2==0, result))
    return list(map(lambda x: x**2, result))

print(evens_double(nums))
```

결과 : **Pass**