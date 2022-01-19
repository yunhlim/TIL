# SWEA 6315. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 8

SWEA 6315. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 8



**문제 : 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.**

```
Input
없음

Output
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

람다식으로 제곱 함수를 만들어주어 출력한다.

```python
nums = list(range(1,11))

def evens(numbers):
    return list(map(lambda x: x**2, numbers))

print(evens(nums))
```

결과 : **Pass**