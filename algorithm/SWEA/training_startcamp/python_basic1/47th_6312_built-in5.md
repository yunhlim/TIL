# SWEA 6312. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 5

---

---

SWEA 6312. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 5



**문제 : 가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고, 단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.**

```
Input
없음

Output
에러발생
```

---

함수에서 여러가지 값의 인자를 입력으로 받기 위해 `*nums`로 받는다. 이러면 nums는 **튜플**형태로 생성된다. 정수가 아닌 값을 구별하기 위해 `map함수`를 사용해 튜플 값인 `nums`를 `int`형태로 받는다. `tuple(map(int,nums))`가 nums와 다른 값을 가지게 되면, nums에 정수가 아닌 인수가 있는 것이므로 이 때 *"에러발생"* 키워드를 프린트한다.

```python
def mul(*nums):
  mul_result = 1
  if tuple(map(int,nums)) != nums:
      print("에러발생")
      return 0
  for num in nums:
      mul_result *= num
  print(mul_result)

mul(1,2,'4',3)
```

결과 : **Pass**