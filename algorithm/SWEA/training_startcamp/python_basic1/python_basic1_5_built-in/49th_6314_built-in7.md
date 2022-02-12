# SWEA 6314. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 7

SWEA 6314. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 7



**문제: 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해 짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.**

```
Input
없음

Output
[2, 4, 6, 8, 10]
```

---

연속된 정수의 list를 만들기 위해 `range()`를 사용한다. `range()`를 `list()`로 씌워준다.

`filter(def,list)`는 *list*를 *def*라는 필터를 거쳐 남은 요소들만으로 변환시켜주는 함수이다.

짝수를 나타내는 함수를 한 줄로 정의해주기 위해서 람다식을 활용한다.

filter함수를 그냥 출력하면 **map**과 같이 **filter 객체**가 출력되므로 `list()`를 사용한다.

```
nums = list(range(1,11))

def evens(nums):
    return list(filter(lambda n: n % 2 == 0, nums))
    
print(evens(nums))
```

결과 : **Pass**